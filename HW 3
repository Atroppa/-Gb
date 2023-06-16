###Задача 16###

n = int(input('Введите количество элементов списка: '))
my_list = list(map(int, input('Введите элементы списка через пробел: ').split()))
x = int(input('Введите число х: '))
count = 0
for i in range(n):
    if my_list[i] == x:
        count += 1
print(f'Число {x} встречается в списке {count} раз.')

###Задача 18###

import random
n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите число для поиска "))
my_list = [random.randint(1, 99) for i in range(n)]
print(my_list)
index_el = 0
min_el = abs(x - my_list[0])
for i in range(1, n):
    diff_value = abs(x - my_list[i])
    if diff_value < min_el:
        min_el = diff_value
        index_el = i
print(f"Самый близкий по значению элемент к заданному числу {my_list[index_el]}")

# или вариант без random
n = abs(int(input('Введите количество элементов в массиве: ')))
i = 0
Ai = []
for i in range(n):
    dig = input("Введите одно целое число: ")
    Ai.append(dig)
my_list = list(map(int, Ai))
print(my_list)
x = int(input("Введите число для поиска "))
index_el = 0
min_el = abs(x - my_list[0])
for i in range(1, n):
    diff_value = abs(x - my_list[i])
    if diff_value < min_el:
        min_el = diff_value
        index_el = i
print(f"Самый близкий по значению элемент к заданному числу {my_list[index_el]}")

###Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность

english_dict = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10
}
russian_dict = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10
}
eng_rus_dict = {}
eng_rus_dict.update(english_dict)
eng_rus_dict.update(russian_dict)
count = 0
word = list(input("Введите слово : ").upper())
for char in word:
    if eng_rus_dict.get(char) is not None:
        count += eng_rus_dict[char]
    else:
        continue
print(count)

