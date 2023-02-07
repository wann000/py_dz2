# * 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», 
# возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out

# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 
# 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 
# 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}

input_names = ["Иван Сергеев", "Мария Серова", "Петр Алексеев", "Илья Иванов",
               "Марина Савельева", "Петр Анисимов", "Алина Ветрякова", "Бибочка Аркадьева"]


def handle_lastname(fullname: str, note: dict):
    splitted = fullname.split()
    last_name = splitted[1]

    if last_name[0] not in note:
        note[last_name[0]] = dict()
    handle_firstname(fullname, note[last_name[0]])


def handle_firstname(fullname: str, note: dict):
    if fullname[0] not in note:
        note[fullname[0]] = list()
    note[fullname[0]].append(fullname)


book = dict()
for name in input_names:
    handle_lastname(name, book)
print(book)