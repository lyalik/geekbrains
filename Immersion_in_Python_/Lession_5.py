# # # # # def generator_function(n):
# # # # #     """Функция-генератор, которая генерирует квадраты чисел от 1 до n."""
# # # # #     for i in range(1, n + 1):
# # # # #         yield i ** 2
# # # # #
# # # # # # Пример использования функции-генератора
# # # # # N = int(input("Введите число N: "))
# # # # # print("Квадраты чисел от 1 до N (функция-генератор):")
# # # # # for square in generator_function(N):
# # # # #     print(square)
# # # # #
# # # # # # Пример использования генераторного выражения
# # # # # N = int(input("Введите число N: "))
# # # # # generator_expression = (i ** 2 for i in range(1, N + 1))
# # # # #
# # # # # print("Квадраты чисел от 1 до N (генераторное выражение):")
# # # # # for square in generator_expression:
# # # # #     print(square)
# # # #
# # # # def generator_function(n):
# # # #     """Функция-генератор, которая генерирует квадраты чисел от 1 до n."""
# # # #     for i in range(1, n + 1):
# # # #         yield i ** 2
# # # #
# # # #
# # # # def main():
# # # #     N = int(input("Введите число N: "))
# # # #
# # # #     # Использование функции-генератора
# # # #     print("Квадраты чисел от 1 до N (функция-генератор):")
# # # #     for square in generator_function(N):
# # # #         print(square)
# # # #
# # # #     # Использование генераторного выражения
# # # #     generator_expression = (i ** 2 for i in range(1, N + 1))
# # # #     print("Квадраты чисел от 1 до N (генераторное выражение):")
# # # #     for square in generator_expression:
# # # #         print(square)
# # # #
# # # #
# # # # if __name__ == "__main__":
# # # #     main()
# # #
# # # #2
# # # names = ["Alice", "Bob", "Charlie"]
# # # salary = [5000, 6000, 7000]
# # # bonus = ["10%", "5%", "15%"]
# # #
# # # # Однострочный генератор словаря
# # # result = {name: salary[i] * float(bonus[i].strip('%')) / 100 for i, name in enumerate(names)}
# # #
# # # # Вывод результата
# # # print(result)
# #
# #
# # #3
# # def fibonacci(n):
# #     """Генераторная функция для последовательности чисел Фибоначчи."""
# #     a, b = 0, 1
# #     for _ in range(n):
# #         yield a
# #         a, b = b, a + b
# #
# #
# # def main():
# #     try:
# #         n = int(input("Введите количество чисел Фибоначчи: "))
# #         if n <= 0:
# #             raise ValueError("Количество чисел должно быть положительным целым числом.")
# #
# #         print(f"Первые {n} чисел Фибоначчи:")
# #         for num in fibonacci(n):
# #             print(num)
# #     except ValueError as e:
# #         print(f"Ошибка ввода: {e}")
# #
# #
# # if __name__ == "__main__":
# #     main()
#
# #4
#
# def substrings(s):
#     """Генераторная функция для всех возможных подстрок строки s."""
#     length = len(s)
#     for start in range(length):
#         for end in range(start + 1, length + 1):
#             yield s[start:end]
#
# def main():
#     s = input("Введите строку: ")
#     print("Все возможные подстроки строки:")
#     for substring in substrings(s):
#         print(substring)
#
# if __name__ == "__main__":
#     main()