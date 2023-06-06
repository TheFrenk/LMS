from book import Book
from reader import Reader
from library_card import LibraryCard
from library import Library

# Create instances of books
book1 = Book("Гаррі Поттер і філософський камінь")
book2 = Book("Вбити пересмішника")
book3 = Book("1984")

# Create instances of readers
reader1 = Reader("Джон")
reader2 = Reader("Еліс")

# Create a library instance
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add readers to the library
library.add_reader(reader1)
library.add_reader(reader2)

# Create book requests for readers
due_date = "2023-07-31"
library_card1 = library.issue_book(reader1, book1, due_date)
library_card2 = library.issue_book(reader2, book2, due_date)

# Return a book to the library
library.return_book(library_card1)

# Print information about the library
print(library)