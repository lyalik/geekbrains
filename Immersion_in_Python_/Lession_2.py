# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# # Запрос двух целых чисел у пользователя
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
#
# # Нахождение НОД
# result = gcd(num1, num2)
#
# # Вывод результата
# print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}.")


# def int_to_hex(num):
#     # Определение символов для шестнадцатеричной системы
#     hex_chars = "0123456789ABCDEF"
#
#     # Обработка случая, когда число равно 0
#     if num == 0:
#         return "0"
#
#     # Проверка на отрицательное число
#     is_negative = num < 0
#     if is_negative:
#         num = -num
#
#     # Преобразование числа в шестнадцатеричное представление
#     hex_str = ""
#     while num > 0:
#         remainder = num % 16
#         hex_str = hex_chars[remainder] + hex_str
#         num = num // 16
#
#     # Добавление префикса '-' для отрицательных чисел
#     if is_negative:
#         hex_str = "-" + hex_str
#
#     return hex_str
#
#
# # Запрос целого числа у пользователя
# num = int(input("Введите целое число: "))
#
# # Преобразование числа в шестнадцатеричное представление
# hex_result = int_to_hex(num)
#
# # Вывод результата
# print(f"Шестнадцатеричное представление числа {num}: {hex_result}")
#
# # Проверка с использованием встроенной функции hex
# print(f"Проверка с использованием hex: {hex(num).upper()}")


# def int_to_roman(num):
#     # Определение массивов для числовых значений и их римских эквивалентов
#     values = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4,
#         1
#     ]
#     symbols = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV",
#         "I"
#     ]
#
#     # Результирующая строка для римского представления
#     roman_str = ""
#
#     # Преобразование числа в римское представление
#     for i in range(len(values)):
#         while num >= values[i]:
#             roman_str += symbols[i]
#             num -= values[i]
#
#     return roman_str
#
#
# # Запрос целого числа у пользователя
# num = int(input("Введите целое число: "))
#
# # Преобразование числа в римское представление
# roman_result = int_to_roman(num)
#
# # Вывод результата
# print(f"Римское представление числа {num}: {roman_result}")



# from fractions import Fraction
#
# def parse_fraction(fraction_str):
#     # Разделение строки на числитель и знаменатель
#     numerator, denominator = map(int, fraction_str.split('/'))
#     return Fraction(numerator, denominator)
#
# # Запрос двух дробей у пользователя
# fraction1_str = input("Введите первую дробь (в формате a/b): ")
# fraction2_str = input("Введите вторую дробь (в формате a/b): ")
#
# # Преобразование строк в объекты Fraction
# fraction1 = parse_fraction(fraction1_str)
# fraction2 = parse_fraction(fraction2_str)
#
# # Нахождение суммы и произведения дробей
# sum_result = fraction1 + fraction2
# product_result = fraction1 * fraction2
#
# # Вывод результатов
# print(f"Сумма дробей {fraction1_str} и {fraction2_str} равна {sum_result}")
# print(f"Произведение дробей {fraction1_str} и {fraction2_str} равно {product_result}")



