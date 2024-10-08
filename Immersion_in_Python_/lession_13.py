# # # # # import random
# # # # #
# # # # # # Определение пользовательских исключений
# # # # # class KillError(Exception):
# # # # #     pass
# # # # #
# # # # # class DrunkError(Exception):
# # # # #     pass
# # # # #
# # # # # class CarCrashError(Exception):
# # # # #     pass
# # # # #
# # # # # class GluttonyError(Exception):
# # # # #     pass
# # # # #
# # # # # class DepressionError(Exception):
# # # # #     pass
# # # # #
# # # # # # Константа для достижения просветления
# # # # # KARMA_GOAL = 500
# # # # #
# # # # # def one_day():
# # # # #     if random.randint(1, 10) == 1:
# # # # #         # Случайное исключение
# # # # #         raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])()
# # # # #     return random.randint(1, 7)
# # # # #
# # # # # def main():
# # # # #     karma = 0
# # # # #
# # # # #     with open("karma.log", "a") as log_file:
# # # # #         while karma < KARMA_GOAL:
# # # # #             try:
# # # # #                 karma += one_day()
# # # # #             except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
# # # # #                 log_file.write(f"Exception: {e.__class__.__name__}\n")
# # # # #
# # # # #     print("Просветление достигнуто!")
# # # # #
# # # # # if __name__ == "__main__":
# # # # #     main()
# # # #
# # # # #2
# # # #
# # # # import os
# # # #
# # # # CHAT_FILE = "chat.txt"
# # # #
# # # # def display_chat():
# # # #     """Функция для отображения текущего текста чата."""
# # # #     if os.path.exists(CHAT_FILE):
# # # #         with open(CHAT_FILE, "r", encoding="utf-8") as file:
# # # #             chat_content = file.read()
# # # #             print("\n--- Текущий текст чата ---")
# # # #             print(chat_content if chat_content else "Чат пуст.")
# # # #             print("--------------------------\n")
# # # #     else:
# # # #         print("\nЧат пуст.\n")
# # # #
# # # # def send_message(username):
# # # #     """Функция для отправки сообщения в чат."""
# # # #     message = input("Введите ваше сообщение: ")
# # # #     with open(CHAT_FILE, "a", encoding="utf-8") as file:
# # # #         file.write(f"{username}: {message}\n")
# # # #     print("Сообщение отправлено!\n")
# # # #
# # # # def main():
# # # #     username = input("Введите ваше имя: ")
# # # #     print(f"Добро пожаловать в чат, {username}!\n")
# # # #
# # # #     while True:
# # # #         print("Выберите действие:")
# # # #         print("1. Посмотреть текущий текст чата")
# # # #         print("2. Отправить сообщение")
# # # #         print("3. Выйти из чата")
# # # #         choice = input("Ваш выбор: ")
# # # #
# # # #         if choice == "1":
# # # #             display_chat()
# # # #         elif choice == "2":
# # # #             send_message(username)
# # # #         elif choice == "3":
# # # #             print("Выход из чата. До свидания!")
# # # #             break
# # # #         else:
# # # #             print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.\n")
# # # #
# # # # if __name__ == "__main__":
# # # #     main()
# # #
# # # import random
# # #
# # # class RandomException(Exception):
# # #     pass
# # #
# # # def main():
# # #     total_sum = 0
# # #     file_name = "numbers.txt"
# # #
# # #     with open(file_name, "a", encoding="utf-8") as file:
# # #         while total_sum < 777:
# # #             try:
# # #                 # С вероятностью 1 к 13 выбрасываем исключение
# # #                 if random.randint(1, 13) == 1:
# # #                     raise RandomException("Вас постигла неудача!")
# # #
# # #                 number = int(input("Введите число: "))
# # #                 total_sum += number
# # #                 file.write(f"{number}\n")
# # #
# # #             except RandomException as e:
# # #                 print(e)
# # #                 print("Программа завершена из-за случайного исключения.")
# # #                 break
# # #             except ValueError:
# # #                 print("Пожалуйста, введите корректное целое число.")
# # #
# # #     if total_sum >= 777:
# # #         print("Поздравляем! Сумма чисел достигла 777 или больше.")
# # #
# # # if __name__ == "__main__":
# # #     main()
# #
# # #3
# #
# # class ScoreLimitExceededError(Exception):
# #     """Исключение для превышения лимита добавляемых очков."""
# #     pass
# #
# # class GameScore:
# #     def __init__(self):
# #         self._score = 0
# #
# #     def add_points(self, points):
# #         if points > 1000:
# #             raise ScoreLimitExceededError("Нельзя добавить больше 1000 очков за раз.")
# #         self._score += points
# #         print(f"Добавлено {points} очков. Текущий счет: {self._score}")
# #
# #     def subtract_points(self, points):
# #         if self._score - points < 0:
# #             raise ValueError("Очки не могут быть отрицательными.")
# #         self._score -= points
# #         print(f"Уменьшено на {points} очков. Текущий счет: {self._score}")
# #
# #     @property
# #     def score(self):
# #         return self._score
# #
# # # Пример использования
# # try:
# #     game_score = GameScore()
# #     game_score.add_points(500)
# #     game_score.add_points(600) # Это вызовет исключение ScoreLimitExceededError
# # except ScoreLimitExceededError as e:
# #     print(e)
# #
# # try:
# #     game_score.subtract_points(200)
# #     game_score.subtract_points(400) # Это вызовет ValueError, так как очки не могут быть отрицательными
# # except ValueError as e:
# #     print(e)
#
#
# #4
#
# class NameError(Exception):
#     """Исключение для некорректного имени."""
#     pass
#
# class EmailError(Exception):
#     """Исключение для некорректного email."""
#     pass
#
# class AgeError(Exception):
#     """Исключение для некорректного возраста."""
#     pass
#
# class User:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         words = value.split()
#         if len(words) < 2 or not all(word.istitle() for word in words):
#             raise NameError("Имя должно состоять из двух слов, каждое из которых начинается с заглавной буквы.")
#         self._name = value
#
#     @property
#     def email(self):
#         return self._email
#
#     @email.setter
#     def email(self, value):
#         if '@' not in value or '.' not in value.split('@')[-1]:
#             raise EmailError("Email должен содержать символ '@' и точку '.' после '@'.")
#         self._email = value
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or not (0 <= value <= 120):
#             raise AgeError("Возраст должен быть положительным целым числом от 0 до 120.")
#         self._age = value
#
#     def __str__(self):
#         return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"
#
# # Пример использования
# try:
#     user = User("Иван Иванов", "ivan@example.com", 25)
#     print(user)
#
#     # Попытка установить некорректные значения
#     user.name = "иван" # Ошибка: имя должно состоять из двух слов, каждое из которых начинается с заглавной буквы
# except NameError as e:
#     print(e)
#
# try:
#     user.email = "ivanexample.com" # Ошибка: email должен содержать символ '@' и точку '.' после '@'
# except EmailError as e:
#     print(e)
#
# try:
#     user.age = 130 # Ошибка: возраст должен быть в диапазоне от 0 до 120
# except AgeError as e:
#     print(e)