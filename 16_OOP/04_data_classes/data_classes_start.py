from dataclasses import dataclass


@dataclass      # decorator to set data class > 3.7
class Book:
    title: str      # typehints > 3.5
    author: str
    pages: int
    price: float

    # regular method
    def bookinfo(self):
        return f"{self.title}, by {self.author}"


b1 = Book("War and Peace", "Leo Tolstroy", 1225, 39.0)
b2 = Book("The Cather in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstroy", 1225, 39.0)

print(b1.title)
print(b2.author)

# data classes implements __repr
print(b1)

# data classes implements __eq
print(b1 == b3)

# changes some field
b1. title = "Anna Karenina"
b1. pages = 864
print(b1.bookinfo())
