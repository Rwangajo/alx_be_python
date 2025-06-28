# library_management.py

class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title, author):
        self.title = title  # Public attribute for the book's title
        self.author = author  # Public attribute for the book's author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out.
        Returns True if the book was successfully checked out, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available (returned).
        Returns True if the book was successfully returned, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available.
        Returns True if available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects, allowing books to be added,
    checked out, returned, and listed by their availability.
    """
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Adds a new Book object to the library's collection.
        Args:
            book (Book): An instance of the Book class to be added.
        """
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.
        Args:
            title (str): The title of the book to check out.
        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Error: Book with title '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Attempts to return a book by its title.
        Args:
            title (str): The title of the book to return.
        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Error: Book with title '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """
        Prints a list of all books currently available (not checked out).
        """
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book)
                available_found = True
        if not available_found:
            print("No books are currently available.")

