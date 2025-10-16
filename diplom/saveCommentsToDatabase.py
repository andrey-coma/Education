import pandas as pd
import datetime
import pendulum
from airflow.models.param import Param
import os
import requests
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
import psycopg2
import re
from datetime import datetime as dt
import logging
# from airflow.operators import BashOperator
from airflow.operators.bash import BashOperator
import sys
import pickle
import interpretable_tsne

sys.path.append('/home/lukyanova/airflow/dags')

# 1. Создание dag
@dag(
    dag_id="saveCommentsToDB",
    schedule_interval="0 0 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    )

def processData():
       
    # Создание в БД (при отсутствии) таблиц "Категории", "Товары", "Комментарии"
    createTables = PostgresOperator(
        task_id="createTables",
        postgres_conn_id="pg_conn",
        sql="""
            CREATE TABLE IF NOT EXISTS comments (
                "id" SERIAL PRIMARY KEY,
                "author"	TEXT,
                "comment"	TEXT,
                "category"  TEXT,
                "category_id" NUMERIC,
                "date"      DATE,
                "card"      TEXT,
                "url"	TEXT,
                "product"	TEXT,
                "product_id" NUMERIC,
                "stars" NUMERIC,
                "price"	NUMERIC,
                "currency" TEXT,
                "weight"	TEXT,
                "processed"	BOOLEAN
            );
          """,
    )
    
    @task
    def LoadData():
        # 2. Чтение данных из файлов
        try:
            # Чтение данных из файла
            # df_comments = pd.read_csv("/home/lukyanova/airflow/dags/data/vkus_vils_products.csv", sep=',')
            df_comments = pd.read_csv("/home/lukyanova/airflow/dags/data/test.csv", sep=',')
            df_comments['card'] = df_comments['date']
            df_comments['processed'] = "0"
           
            # Создание соединения 
            postgres_hook = PostgresHook(postgres_conn_id="pg_conn")
            conn = postgres_hook.get_conn()
            cur = conn.cursor()
            # print(f'df_count = {df}')
            # Вставка данных в БД
            with conn.cursor() as c:
                psycopg2.extras.execute_values(
                    cur=c,
                    sql="""
                        INSERT INTO comments
                        (author, comment, category, card, url, product, stars, price, currency, weight, processed)
                        VALUES %s;
                        """,
                    argslist=df_comments.to_dict(orient="records"),
                    template="""
                        (
                            %(author)s, %(comment)s, %(category)s, %(card)s, %(url)s,
                            %(product)s, %(stars)s, %(price)s,
                            %(currency)s, %(weight)s, %(processed)s
                        )
                        """
                )
            conn.commit()
            return 0
        except Exception as e:
            print(f'!!!! exception {e}')
            return 1

    # Нормализация данных
    fillDataComments = PostgresOperator(
        task_id="fillDataComments",
        postgres_conn_id="pg_conn",
        sql="""
            UPDATE comments SET weight = replace(weight, '/', '') WHERE date is null; commit; 
            UPDATE comments SET date = TO_DATE(trim(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(SUBSTRING(card, 1, length(card) - STRPOS(card, 'Карта'))
                                                , 'янв', '01') , 'фев', '02')
                                                , 'мар', '03'), 'апр', '04')
                                                , 'мая', '05'), 'июн', '06')
                                                , 'июл', '07'), 'авг', '08')
                                                , 'сен', '09'), 'окт', '10')
                                                , 'ноя', '11'), 'окт', '12'), ' ', '-')), 'dd-mm-yyyy')
            WHERE date is null; commit;
            

            UPDATE comments SET card = SUBSTRING(card, STRPOS(card, 'Карта') + 7)  WHERE date is not null; commit;
            """,
    )
    # Разнесение данных из промежуточной таблицы в итоговые
    transferDataToTables = PostgresOperator(
        task_id="transferDataToTables",
        postgres_conn_id="pg_conn",
        sql="""
            -- Добавление категорий (при отсутствии)
            MERGE INTO categories AS cat
            USING (select distinct category from comments) AS com
            ON name = com.category
            WHEN NOT MATCHED THEN 
                INSERT (name) VALUES (com.category); commit;

            -- Заполнение ссылок на категории
            UPDATE comments AS com 
            SET category_id = (SELECT id 
                                FROM categories AS cat 
                                WHERE cat.name = com.category);
            COMMIT;

            -- Добавление товаров (при отсутствии)
            MERGE INTO products AS prod
            USING (select distinct product, category_id from comments) AS com
            ON name = com.product
            AND category = com.category_id
            WHEN NOT MATCHED THEN 
                INSERT (name, category) VALUES (com.product, com.category_id); 
            COMMIT;

            -- Заполнение ссылок на продукты
            UPDATE comments AS com 
            SET product_id = (SELECT id 
                                FROM products AS prod 
                                WHERE prod.name = com.product
                                AND prod.category = com.category_id);
            COMMIT;

            -- Вставка записей в таблицу reviews
            WITH upd AS (
            SELECT author
                , comment
                , card
                , url
                , product_id
                , stars
                , price
                , currency
                , weight 
            FROM comments
            )
            INSERT INTO reviews (author, comment, card, url, product, stars, price, currency, weight, date_add) 
            SELECT *, current_timestamp FROM upd;
            COMMIT;
            DELETE FROM comments;
            COMMIT;
            """,
    )

    # Запуск модели на добавленных данных
    predictAndSave = BashOperator(
    task_id='predictAndSave',
    bash_command='python /home/lukyanova/airflow/dags/predict_results.py')
    print(f'Success predict and save')

    [createTables] >> LoadData() >> [fillDataComments, transferDataToTables, predictAndSave]
# 4. Запуск dag
processData()