# # # import logging
# # #
# # # # Создаем логгер
# # # logger = logging.getLogger("multi_file_logger")
# # # logger.setLevel(logging.DEBUG) # Устанавливаем минимальный уровень логирования для логгера
# # #
# # # # Создаем обработчик для debug_info.log
# # # debug_info_handler = logging.FileHandler("debug_info.log")
# # # debug_info_handler.setLevel(logging.DEBUG) # Устанавливаем уровень логирования для обработчика
# # #
# # # # Создаем обработчик для warnings_errors.log
# # # warnings_errors_handler = logging.FileHandler("warnings_errors.log")
# # # warnings_errors_handler.setLevel(logging.WARNING) # Устанавливаем уровень логирования для обработчика
# # #
# # # # Настраиваем формат сообщений
# # # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# # #
# # # # Применяем формат к обработчикам
# # # debug_info_handler.setFormatter(formatter)
# # # warnings_errors_handler.setFormatter(formatter)
# # #
# # # # Добавляем обработчики к логгеру
# # # logger.addHandler(debug_info_handler)
# # # logger.addHandler(warnings_errors_handler)
# # #
# # # # Пример логирования сообщений разных уровней
# # # logger.debug("Это сообщение уровня DEBUG")
# # # logger.info("Это сообщение уровня INFO")
# # # logger.warning("Это сообщение уровня WARNING")
# # # logger.error("Это сообщение уровня ERROR")
# # # logger.critical("Это сообщение уровня CRITICAL")
# # #
# # # #2
# # #
# # # from datetime import datetime
# # #
# # # # Получаем текущее время и дату
# # # current_datetime = datetime.now()
# # #
# # # # Форматируем дату и время в строку 'YYYY-MM-DD HH:MM:SS'
# # # formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
# # #
# # # # Получаем название дня недели
# # # day_of_week = current_datetime.strftime('%A')
# # #
# # # # Получаем номер недели в году
# # # week_number = current_datetime.isocalendar()[1]
# # #
# # # # Выводим результаты
# # # print(f"Текущая дата и время: {formatted_datetime}")
# # # print(f"День недели: {day_of_week}")
# # # print(f"Номер недели в году: {week_number}")
# #
# # #3
# #
# # from datetime import datetime, timedelta
# #
# # def get_future_date(days_from_now):
# #     """
# #     Возвращает дату, которая наступит через указанное количество дней от текущей даты.
# #
# #     :param days_from_now: Количество дней от текущей даты
# #     :return: Дата в формате 'YYYY-MM-DD'
# #     """
# #     # Получаем текущую дату и время
# #     current_date = datetime.now()
# #
# #     # Создаем объект timedelta с указанным количеством дней
# #     future_timedelta = timedelta(days=days_from_now)
# #
# #     # Вычисляем будущую дату
# #     future_date = current_date + future_timedelta
# #
# #     # Форматируем будущую дату в строку 'YYYY-MM-DD'
# #     formatted_future_date = future_date.strftime('%Y-%m-%d')
# #
# #     return formatted_future_date
# #
# # # Пример использования функции
# # days = 10
# # future_date = get_future_date(days)
# # print(f"Дата через {days} дней: {future_date}")
#
# #4
#
# import argparse
#
# def main():
#     # Создаем объект парсера
#     parser = argparse.ArgumentParser(description="Обработка аргументов командной строки.")
#
#     # Добавляем обязательные аргументы
#     parser.add_argument('number', type=int, help='Число, которое будет обработано.')
#     parser.add_argument('text', type=str, help='Строка, которая будет выведена.')
#
#     # Добавляем опцию --verbose
#     parser.add_argument('--verbose', action='store_true', help='Выводить дополнительную информацию.')
#
#     # Добавляем опцию --repeat
#     parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки.')
#
#     # Парсим аргументы
#     args = parser.parse_args()
#
#     # Обработка флага --verbose
#     if args.verbose:
#         print(f"Получено число: {args.number}")
#         print(f"Получена строка: {args.text}")
#         print(f"Количество повторений: {args.repeat}")
#
#     # Вывод строки указанное количество раз
#     for _ in range(args.repeat):
#         print(args.text)
#
# if __name__ == "__main__":
#     main()
#Проверка
# #python Lession_15.py 5 "Hello, World!" --verbose --repeat 3

#5
import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def collect_directory_info(directory_path):
    if not os.path.isdir(directory_path):
        logging.error(f"Указанный путь не является директорией: {directory_path}")
        return

    parent_directory = os.path.basename(directory_path)
    contents = []

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)
        name, extension = os.path.splitext(item)
        extension = extension.lstrip('.') # Убираем начальную точку из расширения

        file_info = FileInfo(name=name, extension=extension if not is_directory else '', is_directory=is_directory, parent_directory=parent_directory)
        contents.append(file_info)

        # Логирование информации
        logging.info(f"Обработан элемент: {file_info}")

    return contents

if __name__ == "__main__":
    import argparse
