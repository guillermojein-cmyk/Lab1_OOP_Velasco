class LibraryBook:
    # Class attribute/counter para bilangin ang kabuuang librong nagawa
    total_books = 0

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        LibraryBook.total_books += 1  # Dinaragdagan ang counter kapag gumawa ng libro

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return f"Successfully borrowed '{self.title}'. Remaining copies: {self.copies}"
        return f"Sorry, '{self.title}' is currently out of stock."

    def return_book(self):
        self.copies += 1
        return f"Successfully returned '{self.title}'. Available copies: {self.copies}"

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.copies} available)"

    def __repr__(self):
        return f"LibraryBook(title='{self.title}', author='{self.author}', copies={self.copies})"


if __name__ == "__main__":
    print("=== TESTING PART 4: LIBRARY BOOK (MYTHOLOGY) ===")
    
    # Ginamit natin ang librong tungkol sa Mythology
    book1 = LibraryBook("Norse Mythology", "Neil Gaiman", 3)
    
    print(book1)
    print(book1.borrow())
    print(book1.borrow())
    print(book1.return_book())
    print(repr(book1))
    print(f"Total book instances created: {LibraryBook.total_books}")