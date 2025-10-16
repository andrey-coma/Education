# Импорт неоходимых библиотек
import pandas as pd
import re

# # Векторизация текстовых данных TF-IDF
# from sklearn.feature_extraction.text import TfidfVectorizer

# # Нормализация по длине документа
# from sklearn.preprocessing import normalize
# # Преобразование в разреженную матрицу
# from scipy.sparse import csr_matrix

# # Метрики
# from sklearn.metrics import (accuracy_score, f1_score, classification_report, confusion_matrix, ConfusionMatrixDisplay, roc_curve)

# # Понижение размерности
# from sklearn.manifold import TSNE

# # Лингивистические модули
# from razdel import tokenize # сегментация русскоязычного текста на токены и предложения
# import pymorphy3  # Морфологический анализатор
# import pi # лингивистический модуль nltk 
# import nltk
# from nltk.corpus import stopwords # импортируем стоп-слова

import sqlalchemy
import psycopg2
# import pandas as pd
# import sys
# from joblib import dump, load

# Подготовка функций

# # Функция разметки коментариев с использованим поля stars (от 1-3 негивный отзыв, от 4-5 позитивный отзыв)
# def get_label_target(num_stars: int) -> int:
#     if num_stars in (1, 2, 3):
#         return 0  # отзыв негативный
#     else:
#         return 1  # отзыв позитивный


# # Функция очистки отзывов от лишних пробелов, символов и тд. и тп
# def clean_text(text):
#     '''
#     очистка текста
#     на выходе очищеный текст
#     '''
#     if not isinstance(text, str):
#         text = str(text)
    
#     text = text.lower()
#     text = text.strip('\n').strip('\r').strip('\t')
#     text = re.sub("-\s\r\n\|-\s\r\n|\r\n", '', str(text))
#     text = re.sub("[0-9]|[-—.,:;_%©«»?*!@#№$^•·&()]|[+=]|[[]|[]]|[/]|", '', text)
#     text = re.sub(r"\r\n\t|\n|\\s|\r\t|\\n", ' ', text)
#     text = re.sub(r'[\xad]|[\s+]', ' ', text.strip())
#     text = re.sub('n', ' ', text)
    
#     return text


# # Функция токенизации, лемматизация, удаления стоп-слов
# cache = {}
# morph = pymorphy3.MorphAnalyzer()

# def lemmatization(text: str) -> str:
#     '''
#     лемматизация
#         [0] если зашел тип не `str` делаем его `str`
#         [1] токенизация предложения через razdel
#         [2] проверка есть ли в начале слова '-'
#         [3] проверка токена с одного символа
#         [4] проверка есть ли данное слово в кэше
#         [5] лемматизация слова
#         [6] проверка на стоп-слова
#     на выходе лист отлемматизированых токенов
#     '''
#     # [0]
#     if not isinstance(text, str):
#         text = str(text)
    
#     # [1]
#     tokens = list(tokenize(text))
#     words = [_.text for _ in tokens]

#     words_lem = []
    
#     for w in words:
#         if w[0] == '-': # [2]
#             w = w[1:]
#         if len(w) > 1: # [3]
#             if w in cache: # [4]
#                 words_lem.append(cache[w])
#             else: # [5]
#                 temp_cach = cache[w] = morph.parse(w)[0].normal_form
#                 words_lem.append(temp_cach)
    
#     words_lem_without_stopwords=[i for i in words_lem if not i in stopwords_ru] # [6]
    
#     return words_lem_without_stopwords

# # Создадим список стоп-слов из модуля NLTK
# nltk.download('stopwords')
# stopwords_ru = stopwords.words('russian')

# # Уберем частицу не из словаря стоп-слов
# stopwords_ru.remove('не')

# # Дополним стоп-слова из внешнего локального словаря
# with open('/home/lukyanova/airflow/dags/stopwords.txt') as f:
#     additional_stopwords = [w.strip() for w in f.readlines() if w]
    
# stopwords_ru += additional_stopwords

# Параметры подключения к БД (в целевом решении логин/пароль шифровать)
param_dic = {
    "host"      : "localhost",
    "database"  : "airflow_db",
    "user"      : "airflow_user",
    "password"  : "Airflow_user456"
}

# Подключение к БД
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn


# Создание датафрейма на основе данных из БД
def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df

#  Подключение к БД
conn = connect(param_dic)
# Список колонок таблицы
column_names = ["id", "author", "comment", "card", "url", "product", "stars", "price", "currency", "weight", "date_add", "status"]
# Выполнение запроса
df = postgresql_to_dataframe(conn, "select * from reviews", column_names)

# # Предварительная обработка
# df['target'] = df['stars'].apply(get_label_target) # Создаем колонку с целевой переменной "target_by_stars"
# df['comment_pre_processing'] = df['comment'].apply(lambda x: clean_text(x)) # очищенными от лишних данных 
# df['comment_pre_processing'] = df['comment_pre_processing'].apply(lambda x: lemmatization(x)) # применим функцию lemmatization
# df['comment_pre_processing'] = df['comment_pre_processing'].apply(lambda x: ' '.join(x)) # приведем знаячения к строкам
# df.dropna(subset=['comment_pre_processing'], inplace=True) # удалим пропуски в процессе лемматизации (при их наличии)

# tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, max_features=None) # Применение TF-IDF к признаку 'comment_pre_processing'
# df_tfidf_matrix = tfidf_vectorizer.fit_transform(df['comment_pre_processing'])
# # Нормализация матрицы TF-IDF по длине документа

# df_tfidf_matrix_normalized = normalize(df_tfidf_matrix, norm='l2', axis=1)
# # Преобразование в разреженную матрицу
# sparse_matrix = csr_matrix(df_tfidf_matrix_normalized)
# # Понижение размерности TSNE
# tsne = TSNE(n_components=2, random_state=42, n_jobs=-1, perplexity=20)
# tsne_result = tsne.fit_transform(df_tfidf_matrix.toarray())

# # загружаем модель
# # clf = load('/home/lukyanova/airflow/dags/models/best_model.joblib') 

# # pred = clf.predict(tsne_result)

# df.drop(['comment_pre_processing', 'target'], axis=1, inplace=True) # перед записью в БД удаляем 'comment_pre_processing'
# # df['status'] = pred # добавляем колонку с предсказаниями 'status'

df['status'] = 81
print("conn.cursor()")
# Обновление значения колонки "status" в БД значениями соответствующей колонки из датафрейма
cur = conn.cursor()
print("for index, row in df.iterrows()")
for index, row in df.iterrows():
    sql = 'update reviews set status = %s where id = %s'
    cur.execute(sql, (row['status'], row['id']))
conn.commit()