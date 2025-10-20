# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize common book attributes."""
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an EBook with file size (in KB)."""
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook with page count."""
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("Only Book, EBook, or PrintBook instances can be added to the library.")
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
