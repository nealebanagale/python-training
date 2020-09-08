# Inheritance - way to inherit attributes and methods from base classes.
#               makes it easy to centralize common functionality in one place
#               instead of having spread out/duplicated across multiple classes

# base classes
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.price = price
#         self.author = author
#         self.pages = pages
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


# class Magazine:
#     def __init__(self, title, publisher, price, period):
#         self.title = title
#         self.price = price
#         self.period = period
#         self.publisher = publisher
class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


# class Newspaper:
#     def __init__(self, title, publisher, price, period):
#         self.title = title
#         self.price = price
#         self.period = period
#         self.publisher = publisher
class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
m1 = Magazine("NY Times", "New York Times Company", 6.0, "Daily")
n1 = Newspaper("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
