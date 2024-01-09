import csv

def load_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print("Файл не найден. Создание нового файла.")
    return contacts

def save_contacts(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def print_contacts(contacts):
    for contact in contacts:
        print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Номер телефона: {contact[3]}")

def search_contacts(contacts, search_key):
    found_contacts = []
    for contact in contacts:
        if search_key.lower() in contact[0].lower() or search_key.lower() in contact[1].lower():
            found_contacts.append(contact)
    return found_contacts

def main():
    filename = 'contacts.txt'
    contacts = load_contacts(filename)

    while True:
        print("\n1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта по имени или фамилии")
        print("4. Экспорт контактов в файл")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print_contacts(contacts)
        elif choice == '2':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            contacts.append([last_name, first_name, middle_name, phone_number])
            print("Контакт добавлен.")
        elif choice == '3':
            search_key = input("Введите имя или фамилию для поиска: ")
            found_contacts = search_contacts(contacts, search_key)
            if found_contacts:
                print("Найденные контакты:")
                print_contacts(found_contacts)
            else:
                print("Контакты не найдены.")
        elif choice == '4':
            save_contacts(filename, contacts)
            print("Контакты экспортированы в файл.")
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()