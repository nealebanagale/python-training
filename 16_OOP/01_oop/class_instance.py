class Book:
    def __init__(self, title, author, pages, price):
        # instance attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # __ - change the name to avoid other used  class
        # name mangling -prefix class name
        self.__secret = "This is a secret attribute"

    # instance methods
    def getPrice(self):
        return self.price

    def setDiscount(self, amount):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
        # _(underscore) - internal/private


b1 = Book("Brave new book", "Leo Tolstoy", 1225, 39.95)
b2 = Book("War and Peace", "JD Salinger", 234, 29.95)
print(b1.getPrice())
print(b2.getPrice())
b2.setDiscount(0.25)
print(b2.getPrice())
# print(b2.__secret)
print(b2._Book__secret)     # name mangling
