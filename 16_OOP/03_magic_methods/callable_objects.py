class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # call object like a function
    # used on objects whose attributes change frequently/modified together
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("War and Peace", "Leo Tolstroy", 39.0)
b2 = Book("The Cather in the Rye", "JD Salinger", 29.95)

# call the object as the function
print(b1)
# changed value by calling the object as function
b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)
