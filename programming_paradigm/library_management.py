import sys

# ---------------- Division Functionality ----------------

def safe_divide(numerator, denominator):
    if denominator == 0:
        return "Error: Cannot divide by zero."
    return numerator / denominator

numerator = 10
denominator = 2
division_result = safe_divide(numerator, denominator)
print(f"Division Result: {division_result}")

# ---------------- Library System ----------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You checked out: {title}")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"You returned: {title}")
                return
        print(f"No record of '{title}' being checked out.")

    def list_available_books(self):
        found = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                found = True
        if not found:
            print("No available books at the moment.")


# ---------------- Command-line Interface ----------------

def main():
    library = Library()
    # Add example books
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

    if len(sys.argv) < 2:
        print("Usage: python library_and_division_tool.py <command>:<book_title>")
        print("Commands: checkout, return, list")
        sys.exit(1)

    command_parts = sys.argv[1].split(':')
    command = command_parts[0].lower()
    title = command_parts[1] if len(command_parts) > 1 else None

    if command == "checkout" and title:
        library.check_out_book(title)
    elif command == "return" and title:
        library.return_book(title)
    elif command == "list":
        library.list_available_books()
    else:
        print("Invalid command or missing book title.")

if __name__ == "__main__":
    main()
