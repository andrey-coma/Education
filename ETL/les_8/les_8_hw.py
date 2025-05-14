import pandas as pd
import datetime
import pymysql
import os

# airflow
from airflow.decorators import task, dag
from airflow.models.param import Param
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.providers.mysql.operators.mysql import MySqlOperator

#2. Создайте новый dag;
@dag(
    dag_id="data",
    start_date=datetime.datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    dagrun_timeout = datetime.timedelta(minutes=30)
    )

def proccess_data():
    
    def transform_data(df_booking, df_client, df_hotel):
        """
        Функция трансформации данных
        """
        # Объедините все таблицы в одну;
        df = df_booking.merge(df_client, on='client_id').merge(df_hotel, on='hotel_id')
        
        #Приведите даты к одному виду;
        df['booking_date'] = pd.to_datetime(df['booking_date'], format='mixed')
        
        # Удалите невалидные строки;
        df.dropna(subset=['booking_cost', 'age'], inplace=True)
        
        # Приведите все валюты к одной;
        coef = 1.1943 # коэфициент обмена GBP -> EUR
        df['booking_cost_euro'] = df.apply(lambda x: x['booking_cost'] if x['currency'] == 'EUR' else x['booking_cost'] * coef, axis=1)
        df['booking_cost_euro'] = round(df['booking_cost_euro'], 2)
    
        # Удалим ненужные колонки;
        df.drop(['booking_cost', 'currency'], axis=1, inplace=True)
        
        df.reset_index
        
        return df
    
      
    create_sql_query="""
            CREATE TABLE IF NOT EXISTS booking (
                client_id	NUMERIC,
                booking_date	DATE,
                room_type TEXT,
                hotel_id	NUMERIC,
                booking_cost_euro NUMERIC,
                age	INT,
                name_x TEXT,
                type	TEXT,
                name_y TEXT,
                address TEXT
            );"""
    
    create_table = MySqlOperator(
        task_id = 'create_booking_table',
        mysql_conn_id='mysql_id',
        sql = create_sql_query,
        )
    
        
    @task
    def read_df():
        """
        Функция загрузки и объденения дата фреймов с послед. сохранением в один df
        """
        df_b = pd.read_csv('/home/w_lander/airflow/dags/data/booking.csv')
        df_c = pd.read_csv('/home/w_lander/airflow/dags/data/client.csv')
        df_h = pd.read_csv('/home/w_lander/airflow/dags/data/hotel.csv')
    
        df = transform_data(df_b, df_c, df_h) # вызов функции для трансформации данных
    
        df.to_csv('/home/w_lander/airflow/dags/data/result.csv', encoding='utf-8', index=False)
    
    @task
    def load_df():
        df = pd.read_csv('/home/w_lander/airflow/dags/data/result.csv')
        mysql_hook = MySqlHook(mysql_conn_id = 'mysql_id')
        connect = mysql_hook.get_conn()
        cur_dev = connect.cursor()
        with connect.cursor() as c:
            pymysql.extras.execute_values(
                cur_dev=c,
                sql="""
                    INSERT INTO booking
                    (client_id, booking_date, room_type, hotel_id, booking_cost_euro, age, name_x, type, name_y, address)
                     VALUES %s;
                    """,
                argslist=df.to_dict(orient="records"),
                template="""
                    (
                        %(client_id)s, %(booking_date)s, %(room_type)s,
                        %(hotel_id)s, %(booking_cost_euro)s, %(currency)s,
                        %(age)s, %(name_x)s, %(type)s, %(name_y)s, %(address)s
                    )
                    """
                    )
        connect.commit()


    [create_table] >> read_df() >> load_df()

proccess_data()