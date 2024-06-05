"""На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Предметы не должны дублироваться.

Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
"""

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1
backpack = {}

# 1 способ
for i in items:
    if items.get(i) <= round(max_weight, 1):
        backpack.update({i: items.get(i)})
        max_weight -= items.get(i)

print(backpack)

#2 способ
for item, val in items.items():
    if val <= round(max_weight, 1):
        backpack[item] = val
        max_weight -= val

print(backpack)

#3 способ
tmp = 0
for i in items.items():
    tmp += i[1]
    if tmp <= max_weight:
        backpack.update([i])
    else:
        tmp -= i[1]

print(backpack)