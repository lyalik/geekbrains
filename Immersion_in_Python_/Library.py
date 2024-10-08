class BookNotFoundError(Exception):
    """Исключение для случая, когда книга не найдена в библиотеке."""
    pass

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title):
        self._books.append(title)

    def remove_book(self, title):
        if title not in self._books:
            raise BookNotFoundError(f"Книга '{title}' не найдена в библиотеке.")
        self._books.remove(title)

    def list_books(self):
        return self._books