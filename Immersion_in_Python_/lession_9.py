# # # # def how_are_you(func):
# # # #     def wrapper(*args, **kwargs):
# # # #         # Спрашиваем у пользователя "Как дела?"
# # # #         input("Как дела? ")
# # # #         # Выводим сообщение
# # # #         print("А у меня не очень! Ладно, держи свою функцию.")
# # # #         # Вызываем декорируемую функцию
# # # #         return func(*args, **kwargs)
# # # #     return wrapper
# # # #
# # # # # Пример использования декоратора
# # # # @how_are_you
# # # # def test():
# # # #     print("<Тут что-то происходит...>")
# # # #
# # # # @how_are_you
# # # # def another_test():
# # # #     print("<Другая функция выполняется...>")
# # # #
# # # # # Проверка работы декоратора
# # # # test()
# # # # another_test()
# # #
# # # #2
# # #
# # # import time
# # # from functools import wraps
# # #
# # # def delay(seconds):
# # #     """Декоратор, который замедляет выполнение функции на заданное количество секунд."""
# # #     def decorator(func):
# # #         @wraps(func)
# # #         def wrapper(*args, **kwargs):
# # #             print(f"Ждём {seconds} секунд(ы) перед выполнением функции '{func.__name__}'...")
# # #             time.sleep(seconds)
# # #             return func(*args, **kwargs)
# # #         return wrapper
# # #     return decorator
# # #
# # # # Пример использования декоратора
# # # @delay(3)
# # # def fetch_data():
# # #     print("Проверка данных на веб-странице...")
# # #
# # # @delay(5)
# # # def another_task():
# # #     print("Выполнение другой задачи...")
# # #
# # # # Проверка работы декоратора
# # # fetch_data()
# # # another_task()
# #
# # #3
# #
# # from functools import wraps
# #
# #
# # def counter(func):
# #     """Декоратор, считающий и выводящий количество вызовов декорируемой функции."""
# #
# #     @wraps(func)
# #     def wrapper(*args, **kwargs):
# #         wrapper.call_count += 1
# #         print(f"Функция '{func.__name__}' была вызвана {wrapper.call_count} раз(а).")
# #         return func(*args, **kwargs)
# #
# #     wrapper.call_count = 0  # Инициализация счётчика вызовов
# #     return wrapper
# #
# #
# # # Пример использования декоратора
# # @counter
# # def example_function():
# #     print("Выполнение функции...")
# #
# #
# # # Проверка работы декоратора
# # example_function()
# # example_function()
# # example_function()
#
# #4
#
# from functools import wraps
#
# def cache(func):
#     """Декоратор, кэширующий результаты вызова функции."""
#     cache_storage = {}
#
#     @wraps(func)
#     def wrapper(*args):
#         if args in cache_storage:
#             print(f"Возвращаем кэшированный результат для аргументов {args}")
#             return cache_storage[args]
#         result = func(*args)
#         cache_storage[args] = result
#         return result
#
#     return wrapper
#
# # Применение декоратора к функции вычисления чисел Фибоначчи
# @cache
# def fibonacci(n):
#     """Рекурсивная функция для вычисления n-го числа Фибоначчи."""
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# # Проверка работы декоратора
# print(fibonacci(10)) # Должно вычислить и закэшировать результаты
# print(fibonacci(10)) # Должно вернуть кэшированный результат
# print(fibonacci(15)) # Должно вычислить и закэшировать результаты