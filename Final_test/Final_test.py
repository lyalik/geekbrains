### 13. Создание классов с инкапсуляцией и наследованием
class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

class DomesticAnimal(Animal):
    pass

class Dog(DomesticAnimal):
    pass

class Cat(DomesticAnimal):
    pass

class Hamster(DomesticAnimal):
    pass

class PackAnimal(Animal):
    pass

class Horse(PackAnimal):
    pass

class Camel(PackAnimal):
    pass

class Donkey(PackAnimal):
    pass


### 14. Программа для работы реестра домашних животных


class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands

class DomesticAnimal(Animal):
    pass

class Dog(DomesticAnimal):
    pass

class Cat(DomesticAnimal):
    pass

class Hamster(DomesticAnimal):
    pass

class PackAnimal(Animal):
    pass

class Horse(PackAnimal):
    pass

class Camel(PackAnimal):
    pass

class Donkey(PackAnimal):
    pass

class Registry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animal_commands(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal.get_commands()
        return None

    def train_animal(self, name, command):
        for animal in self.animals:
            if animal.name == name:
                animal.add_command(command)

def main():
    registry = Registry()

    while True:
        print("1. Завести новое животное")
        print("2. Определить животное в правильный класс")
        print("3. Увидеть список команд, которые выполняет животное")
        print("4. Обучить животное новым командам")
        print("5. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            name = input("Введите имя животного: ")
            birth_date = input("Введите дату рождения животного (YYYY-MM-DD): ")
            animal_type = input("Введите тип животного (Dog, Cat, Hamster, Horse, Camel, Donkey): ")

            if animal_type == "Dog":
                animal = Dog(name, birth_date)
            elif animal_type == "Cat":
                animal = Cat(name, birth_date)
            elif animal_type == "Hamster":
                animal = Hamster(name, birth_date)
            elif animal_type == "Horse":
                animal = Horse(name, birth_date)
            elif animal_type == "Camel":
                animal = Camel(name, birth_date)
            elif animal_type == "Donkey":
                animal = Donkey(name, birth_date)
            else:
                print("Неправильный тип животного")
                continue

            registry.add_animal(animal)
            print(f"{animal_type} {name} добавлен(а) в реестр")

        elif choice == "2":
            name = input("Введите имя животного: ")
            commands = registry.get_animal_commands(name)
            if commands is not None:
                print(f"Команды для {name}: {', '.join(commands)}")
            else:
                print(f"Животное с именем {name} не найдено")

        elif choice == "3":
            name = input("Введите имя животного: ")
            commands = registry.get_animal_commands(name)
            if commands is not None:
                print(f"Команды для {name}: {', '.join(commands)}")
            else:
                print(f"Животное с именем {name} не найдено")

        elif choice == "4":
            name = input("Введите имя животного: ")
            command = input("Введите новую команду: ")
            registry.train_animal(name, command)
            print(f"Животное {name} обучено новой команде: {command}")

        elif choice == "5":
            break

        else:
            print("Неправильный выбор, попробуйте снова")

if __name__ == "__main__":
    main()


### 15. Класс Счетчик с инкапсуляцией и использованием try-with-resources


class Counter:
    def __init__(self):
        self.count = 0
        self.closed = False

    def add(self):
        if self.closed:
            raise Exception("Counter is closed")
        self.count += 1

    def close(self):
        self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def main():
    try:
        with Counter() as counter:
            name = input("Введите имя животного: ")
            birth_date = input("Введите дату рождения животного (YYYY-MM-DD): ")
            animal_type = input("Введите тип животного (Dog, Cat, Hamster, Horse, Camel, Donkey): ")

            if name and birth_date and animal_type:
                counter.add()
                print(f"Животное {name} добавлено. Текущий счетчик: {counter.count}")
            else:
                print("Заполните все поля")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()