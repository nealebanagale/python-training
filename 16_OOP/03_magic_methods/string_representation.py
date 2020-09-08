class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # provide a user-friendly string description of the object
    # used for display
    def __str__(self):  # override
        return f"{self.title} by {self.author}, costs {self.price}"

    # developer-facing string that ideally to recreate the object
    # for debugging purposes/ a lot of detailed
    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"


b1 = Book("War and Peace", "Leo Tolstroy", 39.0)
b2 = Book("The Cather in the Rye", "JD Salinger", 29.95)

print(b1)       # print triggers __str output
print(b2)       # print triggers __str output
print(str(b1))
print(repr(b2))     # calls repr directly
