# def draw_frame(width, height):
#     for i in range(height):
#         for j in range(width):
#             if i == 0 or i == height - 1:
#                 print('-', end='')
#             elif j == 0 or j == width - 1:
#                 print('|', end='')
#             else:
#                 print(' ', end='')
#         print()
#
# width = int(input("Введите ширину рамки: "))
# height = int(input("Введите высоту рамки: "))
#
# draw_frame(width, height)

# def check_triangle(a, b, c):
#     # Проверка существования треугольника
#     if a + b > c and a + c > b and b + c > a:
#         print("Треугольник существует.")
#
#         # Определение типа треугольника
#         if a == b == c:
#             print("Треугольник равносторонний.")
#         elif a == b or a == c or b == c:
#             print("Треугольник равнобедренный.")
#         else:
#             print("Треугольник разносторонний.")
#     else:
#         print("Треугольник не существует.")
#
#
# # Запрос сторон треугольника у пользователя
# a = float(input("Введите длину стороны a: "))
# b = float(input("Введите длину стороны b: "))
# c = float(input("Введите длину стороны c: "))
#
# # Проверка треугольника
# check_triangle(a, b, c)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def count_primes(sequence):
#     count = 0
#     for number in sequence:
#         if is_prime(number):
#             count += 1
#     return count
#
# # Запрос количества чисел у пользователя
# num_count = int(input("Введите количество чисел: "))
#
# # Ввод чисел и создание последовательности
# sequence = []
# for _ in range(num_count):
#     number = int(input("Введите число: "))
#     sequence.append(number)
#
# # Подсчет простых чисел
# prime_count = count_primes(sequence)
#
# # Вывод результата
# print(f"Количество простых чисел в последовательности: {prime_count}")

# def generate_pit(N):
#     for depth in range(1, N + 1):
#         # Левая часть ямы
#         left_part = ''.join(str(i) for i in range(depth, 0, -1))
#
#         # Количество точек
#         dots = '.' * (2 * (N - depth))
#
#         # Правая часть ямы
#         right_part = ''.join(str(i) for i in range(1, depth + 1))
#
#         # Формирование строки ямы
#         pit_row = left_part + dots + right_part
#
#         # Вывод строки ямы
#         print(pit_row)
#
#
# # Запрос числа N у пользователя
# N = int(input("Введите число N: "))
#
# # Генерация и вывод ямы
# generate_pit(N)

# def guess_number():
#     low = 1
#     high = 100
#     attempts = 0
#
#     print("Загадайте число между 1 и 100 (включительно).")
#
#     while low <= high:
#         attempts += 1
#         mid = (low + high) // 2
#         print(f"Твоё число равно, меньше или больше, чем число {mid}?")
#         print("Введите 1, если равно, 2, если больше, 3, если меньше.")
#         response = int(input())
#
#         if response == 1:
#             print(f"Компьютер угадал число {mid} за {attempts} попыток!")
#             return
#         elif response == 2:
#             low = mid + 1
#         elif response == 3:
#             high = mid - 1
#         else:
#             print("Некорректный ввод. Пожалуйста, введите 1, 2 или 3.")
#
#     print("Что-то пошло не так. Пожалуйста, проверьте ваши ответы.")
#
# # Запуск игры
# guess_number()
#
# answer = input("Введите что-нибудь: ")
#
# print(type(answer))
# print(id(answer))
# print(hash(answer))
# help("Hello world!")
# help()
