'''
Найдите выручку компании в зависимости от месяца.
Для этого напишите функцию calc_income_by_month(), которая на вход принимает список с датами и список с выручкой,
а на выходе словарь, где ключи - это месяцы, а значения - это выручка. Используйте аннотирование типов.

Пример

На входе:

dates = ['2021-11-01']
incomes = [100]

После вашего кода будет автоматически добавлено:

print(calc_income_by_month(dates = ['2021-11-01'], incomes = [100]))

На выходе:

{'11': 100}
'''

def calc_income_by_month(dates:list, incomes:list) -> dict:
    result = dict()
    for key, value in zip(dates, incomes):
        if key[5:7] in result:
            result[key[5:7]] += value
        else:
            result[key[5:7]] = value

    return result

print(calc_income_by_month(dates = ['2021-11-01', '2021-11-15', '2021-12-15', '2021-01-15'], incomes = [200, 300, 700, 1200]))