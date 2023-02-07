# Реализовать функцию, возвращающую n шуток, 
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
random.shuffle(nouns)
random.shuffle(adverbs)
random.shuffle(adjectives)

input = int(input("Введите число шуток от 1 до 5 "))

zipped = zip(nouns, adverbs, adjectives)
print(list(zipped)[:input])