# def remove_duplicates(input_list):
#     # Создаем пустой список для хранения уникальных элементов
#     unique_list = []
#
#     # Проходим по каждому элементу в исходном списке
#     for item in input_list:
#         # Если элемент встречается в списке более одного раза и еще не добавлен в уникальный список
#         if input_list.count(item) > 1 and item not in unique_list:
#             unique_list.append(item)
#
#     return unique_list
#
#
# # Пример списка с повторяющимися элементами
# input_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
#
# # Удаление дубликатов
# result_list = remove_duplicates(input_list)
#
# # Вывод результата
# print(f"Исходный список: {input_list}")
# print(f"Список с дублирующимися элементами: {result_list}")



#2

# def find_max_number(numbers_str):
#     # Разделение строки на отдельные числа и преобразование их в целые числа
#     numbers = list(map(int, numbers_str.split()))
#
#     # Инициализация переменной для хранения наибольшего числа
#     max_number = numbers[0]
#
#     # Проход по каждому элементу списка и сравнение с текущим наибольшим числом
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#
#     return max_number
#
#
# # Запрос строки чисел у пользователя
# numbers_str = input("Введите список чисел через пробел: ")
#
# # Поиск наибольшего числа в списке
# max_number = find_max_number(numbers_str)
#
# # Вывод результата
# print(f"Наибольшее число в списке: {max_number}")

#3

# def is_palindrome(s):
#     # Преобразование всех символов в нижний регистр и удаление пробелов
#     s = s.lower().replace(" ", "")
#
#     # Создание пустого множества для хранения символов, которые встречаются нечетное количество раз
#     odd_chars = set()
#
#     # Обработка каждого символа в строке
#     for char in s:
#         if char in odd_chars:
#             odd_chars.remove(char)
#         else:
#             odd_chars.add(char)
#
#     # Проверка размера множества
#     return len(odd_chars) <= 1
#
#
# # Запрос строки у пользователя
# input_str = input("Введите строку: ")
#
# # Проверка, является ли строка палиндромом
# if is_palindrome(input_str):
#     print("Строка является палиндромом.")
# else:
#     print("Строка не является палиндромом.")


#4

import random
import string


# def generate_password(length):
#     # Определение набора символов для пароля
#     characters = string.ascii_letters + string.digits + string.punctuation
#
#     # Генерация случайного пароля
#     password = ''.join(random.choice(characters) for _ in range(length))
#
#     return password
#
#
# # Запрос длины пароля у пользователя
# length = int(input("Введите длину пароля: "))
#
# # Генерация пароля
# password = generate_password(length)
#
# # Вывод результата
# print(f"Сгенерированный пароль: {password}")

#5

# def are_anagrams(word1, word2):
#     # Проверка, равна ли длина двух слов
#     if len(word1) != len(word2):
#         return False
#
#     # Создание словарей для хранения частоты символов каждого слова
#     char_count1 = {}
#     char_count2 = {}
#
#     # Подсчет частоты символов в первом слове
#     for char in word1:
#         char_count1[char] = char_count1.get(char, 0) + 1
#
#     # Подсчет частоты символов во втором слове
#     for char in word2:
#         char_count2[char] = char_count2.get(char, 0) + 1
#
#     # Сравнение словарей
#     return char_count1 == char_count2
#
#
# # Запрос двух слов у пользователя
# word1 = input("Введите первое слово: ").lower()
# word2 = input("Введите второе слово: ").lower()
#
# # Проверка, являются ли слова анаграммами
# if are_anagrams(word1, word2):
#     print("Слова являются анаграммами.")
# else:
#     print("Слова не являются анаграммами.")

