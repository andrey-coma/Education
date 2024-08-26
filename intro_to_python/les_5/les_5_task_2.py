"""
Задача 2. Глубокое копирование
Вы сделали для заказчика структуру сайта по продаже телефонов:

Заказчик рассказал своим коллегам на рынке, и они захотели такой же сайт для
своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за
работу.
Напишите программу, которая запрашивает у клиента количество сайтов, затем
названия продуктов, а после каждого запроса выводит на экран активные
сайты.
Условия:
● учтите, что функция должна уметь работать с разными сайтами (иначе
вам придётся переделывать программу под каждого заказчика заново);
● вы должны получить список, хранящий сайты для разных продуктов (а
значит, для каждого продукта нужно будет первым делом выполнить
глубокое копирование сайта)
"""

import copy
import pprint

site = { 'html': { 'head': { 'title': 'Куплю/продам телефон недорого' },
                   'body': { 'h2': 'У нас самая низкая цена на iPhone','div': 'Купить', 'p': 'Продать'}
                   }
         }

def mike_site(name_site:str, site_cont:dict) -> dict:
    for key, value in site_cont.items():
        if key == 'title':
            site_cont[key] = value.replace('телефон', name_site)
        if key == 'h2':
            site_cont[key] = value.replace('iPhone', name_site)
        if type(value) is dict:
            mike_site(name_site, value)

    return site_cont

data_sites = [site]
sites_count = int(input('Сколько сайтов: ' ))

while sites_count:
    copy_site = copy.deepcopy(site)
    new_site = input('Введите название сайта: ')
    if new_site.isalpha():
        data_sites.append(mike_site(new_site.capitalize(), copy_site))

        sites_count -= 1

    else:
        print('Некорректное название сайта')


pprint.pprint(data_sites)