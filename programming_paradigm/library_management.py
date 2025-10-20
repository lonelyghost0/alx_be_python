class Book:
    def __init__(self, title, author):
        """Initialize a book with a title, author, and availability status."""
        self.title = title              # public attribute
        self.author = author            # public attribute
        self._is_checked_out = False    # private attribute (by convention)

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_checked_out(self):
        """Return True if the book is checked out, otherwise False."""
        return self._is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty book list."""
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return f"'{title}' has been checked out."
        return f"'{title}' is not available."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return f"'{title}' has been returned."
        return f"'{title}' was not checked out."

    def list_available_books(self):
        """Return a list of all available books."""
        available = [book for book in self._books if not book.is_checked_out()]
        if not available:
            return "No books are currently available."
        return [f"{book.title} by {book.author}" for book in available]
