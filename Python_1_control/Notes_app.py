import json

class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text

class NoteManager:
    def __init__(self, filename):
        self.filename = filename

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        note = Note(title, text)
        self.save_note_to_file(note)

    def save_note_to_file(self, note):
        with open(self.filename, 'a') as file:
            data = {'title': note.title, 'text': note.text}
            json.dump(data, file)
            file.write('\n')

    def read_notes_from_file(self):
        with open(self.filename, 'r') as file:
            for line in file:
                data = json.loads(line)
                note = Note(data['title'], data['text'])
                print(f"Заголовок: {note.title}")
                print(f"Текст: {note.text}")
                print()

    def edit_note(self):
        note_id = int(input("Введите идентификатор заметки для редактирования: "))
        new_title = input("Введите новый заголовок заметки: ")
        new_text = input("Введите новый текст заметки: ")
        self.update_note_in_file(note_id, new_title, new_text)

    def update_note_in_file(self, note_id, new_title, new_text):
        notes = []
        with open(self.filename, 'r') as file:
            for line in file:
                data = json.loads(line)
                notes.append(data)

        if note_id < 1 or note_id > len(notes):
            print("Неверный идентификатор заметки")
            return

        notes[note_id - 1]['title'] = new_title
        notes[note_id - 1]['text'] = new_text

        with open(self.filename, 'w') as file:
            for note in notes:
                json.dump(note, file)
                file.write('\n')

    def delete_note(self):
        note_id = int(input("Введите идентификатор заметки для удаления: "))
        self.remove_note_from_file(note_id)

    def remove_note_from_file(self, note_id):
        notes = []
        with open(self.filename, 'r') as file:
            for line in file:
                data = json.loads(line)
                notes.append(data)

        if note_id < 1 or note_id > len(notes):
            print("Неверный идентификатор заметки")
            return

        del notes[note_id - 1]

        with open(self.filename, 'w') as file:
            for note in notes:
                json.dump(note, file)
                file.write('\n')

note_manager = NoteManager('notes.json')

while True:
    print("1. Создать заметку")
    print("2. Просмотреть список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        note_manager.create_note()
    elif choice == '2':
        note_manager.read_notes_from_file()
    elif choice == '3':
        note_manager.edit_note()
    elif choice == '4':
        note_manager.delete_note()
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")