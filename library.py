from book import Book
from reader import Reader
from library_card import LibraryCard

class Library:
    def __init__(self):
        self.books = []
        self.readers = []
        self.library_cards = []
        self.current_identifier = 1

    def add_book(self, book):
        book.set_identifier(self.current_identifier)
        self.books.append(book)
        self.current_identifier += 1

    def add_reader(self, reader):
        reader.set_identifier(self.current_identifier)
        self.readers.append(reader)
        self.current_identifier += 1

    def issue_book(self, reader, book, due_date):
        if book.available:
            book.available = False
            library_card = LibraryCard(reader, book, due_date)
            self.library_cards.append(library_card)
            return library_card
        else:
            return None

    def return_book(self, library_card):
        if library_card in self.library_cards:
            library_card.book.available = True
            self.library_cards.remove(library_card)

    def __str__(self):
        book_list = "\n".join(str(book) for book in self.books)
        reader_list = "\n".join(str(reader) for reader in self.readers)
        library_card_list = "\n".join(str(card) for card in self.library_cards)
        return f"Бібліотека:\nКниги:\n{book_list}\nЧитачі:\n{reader_list}\nЧитацькі квитки:\n{library_card_list}"