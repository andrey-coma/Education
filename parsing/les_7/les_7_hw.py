from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv


options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://www.thingiverse.com/')

time.sleep(2)
inputs = driver.find_element(By.XPATH, '//input[@placeholder="Search Thingiverse"]')
inputs.send_keys('shark')
inputs.send_keys(Keys.ENTER)

first_height = driver.execute_script("return document.body.scrollHeight") # вычисляем высоту страницы
models_data = []

while True:
    # скролл страницы в подвал
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == first_height:
            break

        first_height = new_height

    models = driver.find_elements(By.XPATH, "//div[@class='ItemCardContainer__itemCard--GGbYM item-card-container']")

    # получение инфо по 3d-модели
    for model in models:
        try:
            title_model = model.find_element(By.XPATH, ".//a[starts-with(@class,'ItemCardHeader')]").text
            author = model.find_element(By.XPATH, ".//a[starts-with(@class,'ItemCardContent')]").get_attribute('text')
            likes = int(model.find_element(By.XPATH, ".//div[starts-with(@class,'ButtonCounterWrapper')]").text.replace('K', '000'))
            url =  model.find_element(By.XPATH, ".//a[starts-with(@class,'ItemCardHeader')]").get_attribute('href')

            models_dict = {
                "title_model" : title_model,
                "author": author,
                'likes': likes,
                "url": url
            }

            models_data.append(models_dict)

        except NoSuchElementException as e:
            # print(e)
            pass

    end_page = driver.find_element(By.XPATH, ".//a[@aria-label='Last page']").get_attribute('href')

    if driver.current_url == end_page:
        break

    next_page_button = driver.find_element(By.XPATH, "//a[@aria-label='Next page']")
    actions = ActionChains(driver)
    actions.move_to_element(next_page_button).click()
    actions.perform()

driver.quit()

# сохраняем инфо по 3д моделям в csv файл
with open('3d_models_info.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(('title_model','author','likes', 'url'))

    for model in models_data:
        writer.writerow((model['title_model'],model['author'],model['likes'], model['url']))