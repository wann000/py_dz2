# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect

import random

txt = "абв"
print("Слово которое нужно удалить из текста: ", txt)
num_word = (int(input("Количество слов в тексте: ")))
list_word = []
print("Рандомный текст: ")
for x in range(num_word):
    random_txt = random.sample(txt, 3)
    list_word.append("".join(random_txt))

print(" ".join(list_word))

print("Текст без абв: ")
list_word2 = list(filter(lambda x: txt not in x, list_word))
print(" ".join(list_word2))