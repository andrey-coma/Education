from mod_les_6 import words_count, rem_dup, unique_list, check_date


# Задача 1
test = ['ключи', 'слова', 'подсчета', 'ключи', 'количество']
print(words_count(test))


# Задача 2
a = 'ffssggee'
print(rem_dup(a))


# Задача 3
list_1 = [3, 4, 5]
list_2 = [1, 8, 9, 5, 6]
print(unique_list(x=list_1, y=list_2))

# Задача 4
date = '30.11.2039'

print(check_date(date))
