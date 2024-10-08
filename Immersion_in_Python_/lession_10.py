# class Animal:
#     def __init__(self, name):
#         self.name = name
#
# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         super().__init__(name)
#         self.wingspan = wingspan
#
#     def wing_length(self):
#         return self.wingspan / 2
#
# class Fish(Animal):
#     def __init__(self, name, max_depth):
#         super().__init__(name)
#         self.max_depth = max_depth
#
#     def depth(self):
#         if self.max_depth < 10:
#             return "Мелководная рыба"
#         elif self.max_depth > 100:
#             return "Глубоководная рыба"
#         else:
#             return "Средневодная рыба"
#
# class Mammal(Animal):
#     def __init__(self, name, weight):
#         super().__init__(name)
#         self.weight = weight
#
#     def category(self):
#         if self.weight < 1:
#             return "Малявка"
#         elif self.weight > 200:
#             return "Гигант"
#         else:
#             return "Обычный"
#
# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type, *args):
#         if animal_type == 'Bird':
#             return Bird(*args)
#         elif animal_type == 'Fish':
#             return Fish(*args)
#         elif animal_type == 'Mammal':
#             return Mammal(*args)
#         else:
#             raise ValueError('Недопустимый тип животного')
#
# # Пример использования фабрики
# factory = AnimalFactory()
#
# # Создание птицы
# sparrow = factory.create_animal('Bird', 'Воробей', 30)
# print(f"{sparrow.name}: размах крыльев {sparrow.wingspan}, длина крыла {sparrow.wing_length()}")
#
# # Создание рыбы
# shark = factory.create_animal('Fish', 'Акула', 150)
# print(f"{shark.name}: максимальная глубина {shark.max_depth}, категория {shark.depth()}")
#
# # Создание млекопитающего
# elephant = factory.create_animal('Mammal', 'Слон', 5000)
# print(f"{elephant.name}: вес {elephant.weight}, категория {elephant.category()}")
#
# # Попытка создать недопустимый тип животного
# try:
#     unknown = factory.create_animal('Reptile', 'Ящерица', 5)
# except ValueError as e:
#     print(e)