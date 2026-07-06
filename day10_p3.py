class BookNotFoundError(Exception):
    """Raised when a book is not found in the library."""
    pass


class Library:
    def __init__(self):
        # Instance attribute to store books
        self.books = []

    def add_book(self, book_name):
        if not isinstance(book_name, str) or book_name.strip() == "":
            raise ValueError("Book name must be a non-empty string.")

        self.books.append(book_name)
        print(f'"{book_name}" added successfully.')

    def remove_book(self, book_name):
        if book_name not in self.books:
            raise BookNotFoundError(f'"{book_name}" not found in the library.')

        self.books.remove(book_name)
        print(f'"{book_name}" removed successfully.')

    def search_book(self, book_name):
        if book_name in self.books:
            return True
        return False

    def __str__(self):
        return f"Library has {len(self.books)} book(s)."


# -------------------------
# Example Usage
# -------------------------

input_books = [b.strip() for b in input("Enter book names separated by commas: ").split(",")]
library = Library()

for book in input_books:
    library.add_book(book)
    print(library)

book_to_search = input("enter the book name to search : ").strip()
print(f"Searching for '{book_to_search}': {library.search_book(book_to_search)}")

book_to_remove = input("enter the book name to remove : ").strip()
try:
    library.remove_book(book_to_remove)
    print(library)
except Exception as e:
    print(e)