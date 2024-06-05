'''
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
(после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
'''

text = "Hello world. Hello Python. Hello again."

clear_text = text
nums_symbols = "1234567980.!,'?"
word_dict = {}
total = []

for symbols in nums_symbols:
    for i in text:
        if i == symbols:
            clear_text = clear_text.replace(i, ' ')

bank_words = clear_text.lower().split()

for word in bank_words:
    if word not in word_dict:
        word_dict[word] = bank_words.count(word)

total = sorted(word_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)[:10]

print(total)

# своя сортировка
# sorted_size = 0
#
# while sorted_size < len(total) - 1:
#     index = 0
#     while index < len(total) - 1:
#         if total[index][1] < total[index + 1][1]:
#             total[index], total[index + 1] = total[index + 1], total[index]
#         index += 1
#     sorted_size += 1