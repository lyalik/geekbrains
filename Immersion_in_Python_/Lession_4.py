# def sum_of_digits(number):
#     """Функция для расчёта суммы цифр числа."""
#     total = 0
#     while number > 0:
#         total += number % 10
#         number //= 10
#     return total
#
#
# def max_digit(number):
#     """Функция для нахождения максимальной цифры числа."""
#     max_d = 0
#     while number > 0:
#         digit = number % 10
#         if digit > max_d:
#             max_d = digit
#         number //= 10
#     return max_d
#
#
# def min_digit(number):
#     """Функция для нахождения минимальной цифры числа."""
#     min_d = 9
#     while number > 0:
#         digit = number % 10
#         if digit < min_d:
#             min_d = digit
#         number //= 10
#     return min_d
#
#
# def main():
#     while True:
#         # Запрос числа у пользователя
#         number = int(input("Введите число: "))
#
#         # Запрос действия у пользователя
#         print("Выберите действие:")
#         print("1 - Вывести сумму цифр числа")
#         print("2 - Вывести максимальную цифру числа")
#         print("3 - Вывести минимальную цифру числа")
#         print("0 - Выйти из программы")
#         choice = int(input("Ваш выбор: "))
#
#         if choice == 1:
#             print(f"Сумма цифр числа {number}: {sum_of_digits(number)}")
#         elif choice == 2:
#             print(f"Максимальная цифра числа {number}: {max_digit(number)}")
#         elif choice == 3:
#             print(f"Минимальная цифра числа {number}: {min_digit(number)}")
#         elif choice == 0:
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
#
# if __name__ == "__main__":
#     main()

#2

# import random
#
#
# def rock_paper_scissors():
#     """Игра 'Камень, ножницы, бумага'."""
#     choices = ["камень", "ножницы", "бумага"]
#     computer_choice = random.choice(choices)
#
#     user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
#
#     if user_choice not in choices:
#         print("Неверный выбор. Попробуйте снова.")
#         return
#
#     print(f"Компьютер выбрал: {computer_choice}")
#
#     if user_choice == computer_choice:
#         print("Ничья!")
#     elif (user_choice == "камень" and computer_choice == "ножницы") or \
#             (user_choice == "ножницы" and computer_choice == "бумага") or \
#             (user_choice == "бумага" and computer_choice == "камень"):
#         print("Вы победили!")
#     else:
#         print("Вы проиграли!")
#
#
# def guess_the_number():
#     """Игра 'Угадай число'."""
#     number_to_guess = random.randint(1, 100)
#     attempts = 0
#
#     while True:
#         user_guess = int(input("Угадайте число от 1 до 100: "))
#         attempts += 1
#
#         if user_guess < number_to_guess:
#             print("Загаданное число больше.")
#         elif user_guess > number_to_guess:
#             print("Загаданное число меньше.")
#         else:
#             print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
#             break
#
#
# def main_menu():
#     """Главное меню игры."""
#     while True:
#         print("\nВыберите игру:")
#         print("1 - Камень, ножницы, бумага")
#         print("2 - Угадай число")
#         print("0 - Выйти из программы")
#
#         choice = input("Ваш выбор: ")
#
#         if choice == "1":
#             rock_paper_scissors()
#         elif choice == "2":
#             guess_the_number()
#         elif choice == "0":
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
#
# if __name__ == "__main__":
#     main_menu()

#3

# def reverse_number(x):
#     """Функция для переворачивания числа."""
#     reversed_x = 0
#     while x > 0:
#         reversed_x = reversed_x * 10 + x % 10
#         x //= 10
#     return reversed_x
#
#
# def main():
#     # Запрос чисел у пользователя
#     N = int(input("Введите первое число: "))
#     K = int(input("Введите второе число: "))
#
#     # Переворачивание чисел
#     reversed_N = reverse_number(N)
#     reversed_K = reverse_number(K)
#
#     print(f"Первое число наоборот: {reversed_N}")
#     print(f"Второе число наоборот: {reversed_K}")
#
#     # Сложение перевёрнутых чисел
#     sum_reversed = reversed_N + reversed_K
#     print(f"Сумма: {sum_reversed}")
#
#     # Переворачивание суммы
#     reversed_sum = reverse_number(sum_reversed)
#     print(f"Сумма наоборот: {reversed_sum}")
#
#
# if __name__ == "__main__":
#     main()

#4

# def maximum_of_two(a, b):
#     """Функция для нахождения максимума из двух чисел."""
#     if a > b:
#         return a
#     else:
#         return b
#
# def maximum_of_three(a, b, c):
#     """Функция для нахождения максимума из трёх чисел."""
#     max_of_two = maximum_of_two(a, b)
#     return maximum_of_two(max_of_two, c)
#
# # Пример использования функций
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
#
# max_value = maximum_of_three(num1, num2, num3)
# print(f"Максимальное из трёх чисел: {max_value}")


#5

# def calculate_danger(x):
#     """Функция для расчёта уровня опасности по формуле D = x^3 - 3x^2 - 12x + 10."""
#     return x ** 3 - 3 * x ** 2 - 12 * x + 10
#
#
# def find_safe_depth(max_danger):
#     """Функция для нахождения глубины с уровнем опасности, максимально близким к нулю."""
#     low = 0
#     high = 4
#     mid = (low + high) / 2.0
#
#     while high - low > 1e-7:  # Точность до 1e-7 для более точного результата
#         mid = (low + high) / 2.0
#         danger = calculate_danger(mid)
#
#         if abs(danger) < max_danger:
#             return mid
#
#         if danger > 0:
#             high = mid
#         else:
#             low = mid
#
#     return mid
#
#
# def main():
#     try:
#         max_danger = float(input("Введите максимально допустимый уровень опасности: "))
#         if max_danger < 0:
#             raise ValueError("Уровень опасности должен быть положительным числом.")
#
#         safe_depth = find_safe_depth(max_danger)
#         print(f"Приблизительная глубина безопасной кладки: {safe_depth:.8f} м")
#     except ValueError as e:
#         print(f"Ошибка ввода: {e}")
#
#
# if __name__ == "__main__":
#     main()