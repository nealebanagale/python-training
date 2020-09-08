class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # overrides the equality check between two objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")
        return(self.title == value.title and
               self.author == value.author and
               self.price == value.price
               )

    # grater than or equal
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")

        return self.price >= value.price

    # less than
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")

        return self.price < value.price


b1 = Book("War and Peace", "Leo Tolstroy", 39.95)
b2 = Book("The Cather in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstroy", 39.95)
b4 = Book("To Kill a Mockingbird", "Hardper Lee", 24.95)


# check equality
print(b1 == b3)     # false - compares instances not attributes
print(b1 == b2)
# print(b1 == 42)     # error

# grater and lesser value
print(b2 >= b1)
print(b2 < b1)

# sorting using magic method
books = [b1, b2, b3, b4]
books.sort()    # sorted from low to high of price
print([book.title for book in books])


# ADDITIONAL REFERENCE: https://docs.python.org/3/reference/datamodel.html
