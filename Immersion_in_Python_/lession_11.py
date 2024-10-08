# # # # # class Matrix:
# # # # #     def __init__(self, rows, cols):
# # # # #         self.rows = rows
# # # # #         self.cols = cols
# # # # #         self.data = [[0] * cols for _ in range(rows)]
# # # # #
# # # # #     def __str__(self):
# # # # #         return '\n'.join([' '.join(map(str, row)) for row in self.data])
# # # # #
# # # # #     def add(self, other):
# # # # #         if self.rows != other.rows or self.cols != other.cols:
# # # # #             raise ValueError("Матрицы должны быть одинакового размера для сложения.")
# # # # #         result = Matrix(self.rows, self.cols)
# # # # #         for i in range(self.rows):
# # # # #             for j in range(self.cols):
# # # # #                 result.data[i][j] = self.data[i][j] + other.data[i][j]
# # # # #         return result
# # # # #
# # # # #     def subtract(self, other):
# # # # #         if self.rows != other.rows or self.cols != other.cols:
# # # # #             raise ValueError("Матрицы должны быть одинакового размера для вычитания.")
# # # # #         result = Matrix(self.rows, self.cols)
# # # # #         for i in range(self.rows):
# # # # #             for j in range(self.cols):
# # # # #                 result.data[i][j] = self.data[i][j] - other.data[i][j]
# # # # #         return result
# # # # #
# # # # #     def multiply(self, other):
# # # # #         if self.cols != other.rows:
# # # # #             raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
# # # # #         result = Matrix(self.rows, other.cols)
# # # # #         for i in range(self.rows):
# # # # #             for j in range(other.cols):
# # # # #                 for k in range(self.cols):
# # # # #                     result.data[i][j] += self.data[i][k] * other.data[k][j]
# # # # #         return result
# # # # #
# # # # #     def transpose(self):
# # # # #         result = Matrix(self.cols, self.rows)
# # # # #         for i in range(self.rows):
# # # # #             for j in range(self.cols):
# # # # #                 result.data[j][i] = self.data[i][j]
# # # # #         return result
# # # # #
# # # # # # Создание экземпляров класса Matrix
# # # # # m1 = Matrix(2, 3)
# # # # # m1.data = [[1, 2, 3], [4, 5, 6]]
# # # # # m2 = Matrix(2, 3)
# # # # # m2.data = [[7, 8, 9], [10, 11, 12]]
# # # # #
# # # # # # Тестирование операций
# # # # # print("Матрица 1:")
# # # # # print(m1)
# # # # # print("Матрица 2:")
# # # # # print(m2)
# # # # #
# # # # # print("Сложение матриц:")
# # # # # print(m1.add(m2))
# # # # #
# # # # # print("Вычитание матриц:")
# # # # # print(m1.subtract(m2))
# # # # #
# # # # # m3 = Matrix(3, 2)
# # # # # m3.data = [[1, 2], [3, 4], [5, 6]]
# # # # #
# # # # # print("Умножение матриц:")
# # # # # print(m1.multiply(m3))
# # # # #
# # # # # print("Транспонирование матрицы 1:")
# # # # # print(m1.transpose())
# # # #
# # # # #2
# # # #
# # # # class Water:
# # # #     def __add__(self, other):
# # # #         if isinstance(other, Air):
# # # #             return Storm()
# # # #         elif isinstance(other, Fire):
# # # #             return Steam()
# # # #         elif isinstance(other, Earth):
# # # #             return Mud()
# # # #         elif isinstance(other, Lightning):
# # # #             return Thunderstorm()
# # # #         return None
# # # #
# # # # class Air:
# # # #     def __add__(self, other):
# # # #         if isinstance(other, Water):
# # # #             return Storm()
# # # #         elif isinstance(other, Fire):
# # # #             return Lightning()
# # # #         elif isinstance(other, Earth):
# # # #             return Dust()
# # # #         elif isinstance(other, Lightning):
# # # #             return Thunderstorm()
# # # #         return None
# # # #
# # # # class Fire:
# # # #     def __add__(self, other):
# # # #         if isinstance(other, Water):
# # # #             return Steam()
# # # #         elif isinstance(other, Air):
# # # #             return Lightning()
# # # #         elif isinstance(other, Earth):
# # # #             return Lava()
# # # #         elif isinstance(other, Lightning):
# # # #             return Plasma()
# # # #         return None
# # # #
# # # # class Earth:
# # # #     def __add__(self, other):
# # # #         if isinstance(other, Water):
# # # #             return Mud()
# # # #         elif isinstance(other, Air):
# # # #             return Dust()
# # # #         elif isinstance(other, Fire):
# # # #             return Lava()
# # # #         elif isinstance(other, Lightning):
# # # #             return Glass()
# # # #         return None
# # # #
# # # # class Storm:
# # # #     def __str__(self):
# # # #         return "Шторм"
# # # #
# # # # class Steam:
# # # #     def __str__(self):
# # # #         return "Пар"
# # # #
# # # # class Mud:
# # # #     def __str__(self):
# # # #         return "Грязь"
# # # #
# # # # class Lightning:
# # # #     def __str__(self):
# # # #         return "Молния"
# # # #
# # # # class Dust:
# # # #     def __str__(self):
# # # #         return "Пыль"
# # # #
# # # # class Lava:
# # # #     def __str__(self):
# # # #         return "Лава"
# # # #
# # # # # Новый элемент: Lightning (Молния)
# # # # class Thunderstorm:
# # # #     def __str__(self):
# # # #         return "Гроза"
# # # #
# # # # class Plasma:
# # # #     def __str__(self):
# # # #         return "Плазма"
# # # #
# # # # class Glass:
# # # #     def __str__(self):
# # # #         return "Стекло"
# # # #
# # # # # Пример использования
# # # # water = Water()
# # # # air = Air()
# # # # fire = Fire()
# # # # earth = Earth()
# # # # lightning = Lightning()
# # # #
# # # # print(water + air) # Шторм
# # # # print(water + fire) # Пар
# # # # print(water + earth) # Грязь
# # # # print(air + fire) # Молния
# # # # print(air + earth) # Пыль
# # # # print(fire + earth) # Лава
# # # #
# # # # # Примеры с новым элементом
# # # # print(water + lightning) # Гроза
# # # # print(air + lightning) # Гроза
# # # # print(fire + lightning) # Плазма
# # # # print(earth + lightning) # Стекло
# # #
# # # #3
# # #
# # # class Rectangle:
# # #     def __init__(self, width, height=None):
# # #         self.width = width
# # #         self.height = height if height is not None else width
# # #
# # #     def perimeter(self):
# # #         return 2 * (self.width + self.height)
# # #
# # #     def area(self):
# # #         return self.width * self.height
# # #
# # #     def __add__(self, other):
# # #         new_perimeter = self.perimeter() + other.perimeter()
# # #         new_width = (new_perimeter // 2) // 2
# # #         new_height = new_perimeter // 2 - new_width
# # #         return Rectangle(new_width, new_height)
# # #
# # #     def __sub__(self, other):
# # #         new_perimeter = abs(self.perimeter() - other.perimeter())
# # #         new_width = (new_perimeter // 2) // 2
# # #         new_height = new_perimeter // 2 - new_width
# # #         return Rectangle(new_width, new_height)
# # #
# # #     def __lt__(self, other):
# # #         return self.area() < other.area()
# # #
# # #     def __eq__(self, other):
# # #         return self.area() == other.area()
# # #
# # #     def __le__(self, other):
# # #         return self.area() <= other.area()
# # #
# # #     def __str__(self):
# # #         return f"Прямоугольник со сторонами {self.width} и {self.height}"
# # #
# # #     def __repr__(self):
# # #         return f"Rectangle({self.width}, {self.height})"
# # #
# # # # Пример использования
# # # rect1 = Rectangle(5, 10)
# # # rect2 = Rectangle(3, 7)
# # #
# # # print(f"Периметр rect1: {rect1.perimeter()}")
# # # print(f"Площадь rect2: {rect2.area()}")
# # # print(f"rect1 < rect2: {rect1 < rect2}")
# # # print(f"rect1 == rect2: {rect1 == rect2}")
# # # print(f"rect1 <= rect2: {rect1 <= rect2}")
# # #
# # # rect3 = rect1 + rect2
# # # print(f"Периметр rect3: {rect3.perimeter()}")
# # #
# # # rect4 = rect1 - rect2
# # # print(f"Ширина rect4: {rect4.width}")
# #
# # #4
# #
# # class Stack:
# #     def __init__(self):
# #         self.items = []
# #
# #     def push(self, item):
# #         self.items.append(item)
# #
# #     def pop(self):
# #         if not self.is_empty():
# #             return self.items.pop()
# #         return None
# #
# #     def is_empty(self):
# #         return len(self.items) == 0
# #
# #     def __str__(self):
# #         return str(self.items)
# #
# # class TaskManager:
# #     def __init__(self):
# #         self.tasks = {}
# #
# #     def new_task(self, task, priority):
# #         if priority not in self.tasks:
# #             self.tasks[priority] = Stack()
# #         self.tasks[priority].push(task)
# #
# #     def remove_task(self, task, priority):
# #         if priority in self.tasks:
# #             temp_stack = Stack()
# #             removed = False
# #             while not self.tasks[priority].is_empty():
# #                 current_task = self.tasks[priority].pop()
# #                 if current_task == task and not removed:
# #                     removed = True
# #                 else:
# #                     temp_stack.push(current_task)
# #             while not temp_stack.is_empty():
# #                 self.tasks[priority].push(temp_stack.pop())
# #             if self.tasks[priority].is_empty():
# #                 del self.tasks[priority]
# #
# #     def __str__(self):
# #         result = []
# #         for priority in sorted(self.tasks):
# #             tasks_at_priority = []
# #             temp_stack = Stack()
# #             while not self.tasks[priority].is_empty():
# #                 task = self.tasks[priority].pop()
# #                 tasks_at_priority.append(task)
# #                 temp_stack.push(task)
# #             while not temp_stack.is_empty():
# #                 self.tasks[priority].push(temp_stack.pop())
# #             result.append(f"{priority} — {'; '.join(reversed(tasks_at_priority))}")
# #         return '\n'.join(result)
# #
# # # Пример использования
# # manager = TaskManager()
# # manager.new_task("сделать уборку", 4)
# # manager.new_task("помыть посуду", 4)
# # manager.new_task("отдохнуть", 1)
# # manager.new_task("поесть", 2)
# # manager.new_task("сдать ДЗ", 2)
# #
# # print(manager)
# #
# # # Удаление задачи
# # manager.remove_task("поесть", 2)
# # print("\nПосле удаления задачи 'поесть':")
# # print(manager)
#
# #4
#
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
# # Пример использования
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# triangle = Triangle(3, 7)
#
# print(f"Площадь круга: {circle.area()}")
# print(f"Площадь прямоугольника: {rectangle.area()}")
# print(f"Площадь треугольника: {triangle.area()}")
#
# # Попытка создать объект класса Shape вызовет ошибку
# try:
#     shape = Shape()
# except TypeError as e:
#     print(e)

