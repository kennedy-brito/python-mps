class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class BookCollection:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)

class BookIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration

# Exemplo de uso
collection = BookCollection()
collection.add_book(Book("1984", "George Orwell"))
collection.add_book(Book("Brave New World", "Aldous Huxley"))
collection.add_book(Book("Fahrenheit 451", "Ray Bradbury"))

for book in collection:
    print(book)
