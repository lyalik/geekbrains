# # # # import csv
# # # #
# # # # class NameDescriptor:
# # # #     def __get__(self, instance, owner):
# # # #         return instance.__dict__.get('name')
# # # #
# # # #     def __set__(self, instance, value):
# # # #         if not value.istitle() or not value.replace(' ', '').isalpha():
# # # #             raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
# # # #         instance.__dict__['name'] = value
# # # #
# # # # class Student:
# # # #     name = NameDescriptor()
# # # #
# # # #     def __init__(self, name, subjects_file):
# # # #         self.name = name
# # # #         self.subjects = {}
# # # #         self.load_subjects(subjects_file)
# # # #
# # # #     def load_subjects(self, subjects_file):
# # # #         try:
# # # #             with open(subjects_file, newline='', encoding='utf-8') as csvfile:
# # # #                 reader = csv.reader(csvfile)
# # # #                 for row in reader:
# # # #                     for subject in row:
# # # #                         self.subjects[subject] = {'grades': [], 'tests': []}
# # # #         except FileNotFoundError:
# # # #             print(f"Файл {subjects_file} не найден")
# # # #
# # # #     def add_grade(self, subject, grade):
# # # #         if subject not in self.subjects:
# # # #             print(f"Предмет {subject} не найден")
# # # #             return
# # # #         if not (2 <= grade <= 5):
# # # #             print("Оценка должна быть целым числом от 2 до 5")
# # # #             return
# # # #         self.subjects[subject]['grades'].append(grade)
# # # #
# # # #     def add_test_result(self, subject, result):
# # # #         if subject not in self.subjects:
# # # #             print(f"Предмет {subject} не найден")
# # # #             return
# # # #         if not (0 <= result <= 100):
# # # #             print("Результат теста должен быть целым числом от 0 до 100")
# # # #             return
# # # #         self.subjects[subject]['tests'].append(result)
# # # #
# # # #     def average_test_score(self, subject):
# # # #         if subject not in self.subjects:
# # # #             print(f"Предмет {subject} не найден")
# # # #             return None
# # # #         tests = self.subjects[subject]['tests']
# # # #         return sum(tests) / len(tests) if tests else 0
# # # #
# # # #     def average_grade(self):
# # # #         total_grades = []
# # # #         for subject in self.subjects.values():
# # # #             total_grades.extend(subject['grades'])
# # # #         return sum(total_grades) / len(total_grades) if total_grades else 0
# # # #
# # # #     def __str__(self):
# # # #         subjects_list = ', '.join(self.subjects.keys())
# # # #         return f"Студент: {self.name}\nПредметы: {subjects_list}"
# # # #
# # # # # Пример использования
# # # # student = Student("Иван Иванов", "subjects.csv")
# # # # student.add_grade("Математика", 5)
# # # # student.add_grade("История", 4)
# # # # student.add_test_result("Математика", 90)
# # # # student.add_test_result("История", 85)
# # # #
# # # # print(student)
# # # # print(f"Средний балл по тестам (Математика): {student.average_test_score('Математика')}")
# # # # print(f"Средний балл по всем предметам: {student.average_grade()}")
# # #
# # # #2
# # #
# # # class Person:
# # #     def __init__(self, name, age, email):
# # #         self.name = name
# # #         self.age = age
# # #         self.email = email
# # #
# # #     @property
# # #     def name(self):
# # #         return self._name
# # #
# # #     @name.setter
# # #     def name(self, value):
# # #         if not value.istitle():
# # #             raise ValueError("Имя должно начинаться с заглавной буквы")
# # #         self._name = value
# # #
# # #     @property
# # #     def age(self):
# # #         return self._age
# # #
# # #     @age.setter
# # #     def age(self, value):
# # #         if not isinstance(value, int) or not (0 <= value <= 120):
# # #             raise ValueError("Возраст должен быть целым числом в диапазоне от 0 до 120")
# # #         self._age = value
# # #
# # #     @property
# # #     def email(self):
# # #         return self._email
# # #
# # #     @email.setter
# # #     def email(self, value):
# # #         if '@' not in value:
# # #             raise ValueError("Email должен содержать символ '@'")
# # #         self._email = value
# # #
# # #     def __str__(self):
# # #         return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"
# # #
# # # # Пример использования
# # # try:
# # #     person = Person("Иван", 25, "ivan@example.com")
# # #     print(person)
# # #
# # #     # Попытка установить некорректные значения
# # #     person.name = "иван" # Ошибка: имя должно начинаться с заглавной буквы
# # # except ValueError as e:
# # #     print(e)
# # #
# # # try:
# # #     person.age = 130 # Ошибка: возраст должен быть в диапазоне от 0 до 120
# # # except ValueError as e:
# # #     print(e)
# # #
# # # try:
# # #     person.email = "ivanexample.com" # Ошибка: email должен содержать символ '@'
# # # except ValueError as e:
# # #     print(e)
# #
# # #3
# #
# # class Book:
# #     _id_counter = 0 # Статический атрибут для хранения последнего использованного идентификатора
# #
# #     def __new__(cls, *args, **kwargs):
# #         instance = super().__new__(cls)
# #         instance.id = cls._generate_id()
# #         return instance
# #
# #     @classmethod
# #     def _generate_id(cls):
# #         cls._id_counter += 1
# #         return cls._id_counter
# #
# #     def __init__(self, title, author):
# #         self.title = title
# #         self.author = author
# #
# #     def __str__(self):
# #         return f"Book ID: {self.id}, Title: {self.title}, Author: {self.author}"
# #
# # # Пример использования
# # book1 = Book("1984", "George Orwell")
# # book2 = Book("Brave New World", "Aldous Huxley")
# # book3 = Book("Fahrenheit 451", "Ray Bradbury")
# #
# # print(book1)
# # print(book2)
# # print(book3)
#
# #3
#
