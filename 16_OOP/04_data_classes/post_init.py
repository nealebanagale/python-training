from dataclasses import dataclass


@dataclass      # decorator to set data class > 3.7
class Book:
    title: str      # typehints > 3.5
    author: str
    pages: int
    price: float

    # post_init function
    # - after object has been initialized via built-in __init__
    # - add additional attributes that depend on values of other attributes
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages}"


b1 = Book("War and Peace", "Leo Tolstroy", 1225, 39.0)
b2 = Book("The Cather in the Rye", "JD Salinger", 234, 29.95)

print(b1.description)
print(b2.description)
