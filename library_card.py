class LibraryCard:
    def __init__(self, reader, book, due_date):
        self.reader = reader
        self.book = book
        self.due_date = due_date

    def __str__(self):
        return f"Читацький квиток: {self.reader} запозичено {self.book} (Термін виконання: {self.due_date})"