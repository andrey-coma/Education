from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import csv

url = 'https://vkusvill.ru/goods/griby-shampinony-svezhie-250-g-23719.html'
TOTAL_COMMENT = 130 # Максимальное кол-во отзывов для сбора

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)
driver.get(url) # загружаем стартовую страницу
time.sleep(3) # ожидаем загрузку стартовой страницы

# проматываем на 400 пикселей вниз для появления кнопки отзывы
driver.execute_script("window.scrollBy(0, 400)")
time.sleep(0.5)

# забираем категорию товара
category = driver.find_elements(By.XPATH, ".//span[contains(@class, 'Breadcrumbs__slide')]")[2].text

# нажимаем кнопку отзывы
button = driver.find_element(By.XPATH, "//button[@data-id='vv23-detail-page-tabs-id-2']")
button.click()

# вычисляем высоту страницы
first_height = driver.execute_script("return document.body.scrollHeight")

comments_data = [] # список для отзывов
num_com = 0 # счетчик отзывов

while True:
    # прокрутка страницы в подвал
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3) # ожидаем прокрутку
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == first_height:
            break

        first_height = new_height

    # закрытие модульного окна при 1-ой прокрутке
    if num_com == 0:
        actions = ActionChains(driver)
        actions.move_by_offset(100, 100).perform()
        actions.click().perform()
        time.sleep(1)

    products_comments = driver.find_elements(By.XPATH, "//div[@class='ReviewsApiCat4ListItem js-product-api-review']")
    # получение инфо по продукту
    for item in products_comments[num_com:]:
        try:
            author = item.find_element(By.XPATH, ".//div[contains(@class, 'ReviewsApiCat4ListItemName')]").text
            comment = item.find_element(By.XPATH, ".//div[contains(@class,'ReviewsApiCat4ListItemBody')]").text
            date = item.find_element(By.XPATH, ".//div[contains(@class,'CardDate')]").text
            url = driver.current_url
            product = item.find_element(By.XPATH, "//h1[contains(@class, 'Product__title')]").text
            stars = item.find_element(By.XPATH, ".//div[contains(@class, 'ReviewsApiCat4ListItemRate')]").text
            price_currency_weight = item.find_element(By.XPATH, "//span[contains(@class, 'Price--lg Price--gray')]").text.split('\n')

            comments_dict = {
                'author': author,
                'comment': comment,
                'date': date,
                'url': url,
                'product': product,
                'category': category.split(' ')[0].split(',')[0],
                'stars': stars,
                'price': price_currency_weight[0],
                'currency': price_currency_weight[1],
                'weight': price_currency_weight[2]
            }

            comments_data.append(comments_dict)

        except NoSuchElementException as e:
            # print(e)
            pass

    # если кнопки "показать больше" нет, обрабатываем ошибку NoSuchElementException
    try:
        next_page_button = driver.find_element(By.XPATH, "//button[@title='Загрузить больше']")

        actions = ActionChains(driver)
        actions.move_to_element(next_page_button).click()
        actions.perform()

    except NoSuchElementException as e:
        print(f'По данному продукту всего: {len(comments_data)} отзывов')
        break

    print(f'Обработано отзывов: {len(comments_data)}')

    if len(comments_data) >= TOTAL_COMMENT: # выход из цикла при достижении необх. кол-ва отзывов
        break

    num_com += 10 # исключаем повторный сбор отзывов

driver.quit()

# формируем имя выходного файла
product_name = url.split('/')[4].split('-')
pref = product_name[-1].split('.')

# сохраняем инфо по продукту в csv файл
with open('data_pars_test/products_' + product_name[0] + '_' + pref[0] + '.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(('author','comment','date', 'url', 'product', 'category',
                     'stars', 'price', 'currency', 'weight'))

    for com in comments_data:

        writer.writerow((com['author'],com['comment'],com['date'],
                         com['url'], com['product'], com['category'], com['stars'],
                         com['price'], com['currency'], com['weight']))