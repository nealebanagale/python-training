class Book:
    # class-level attribute
    # all caps to indicate class level attr
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # class method - work on the entire class
    @classmethod    # class method decorator
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # static method - don't modify either the class or specific object instance
    __booklist = None   # __ = private

    @staticmethod
    def getBookList():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods - specific objects
    def setTitle(self, newTitle):
        self.title = newTitle

    def __init__(self, title, booktype):
        self.title = title
        if (booktype not in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.boktype = booktype


# access the class attribute
print("Book type: ", Book.getBookTypes())

# create class instance
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 1", "PAPERBACK")

# access static method (singleton object)
theBooks = Book.getBookList()
theBooks.append(b1)
theBooks.append(b2)
print(theBooks)
