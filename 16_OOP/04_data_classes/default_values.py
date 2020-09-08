from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))   # between 20-40


@dataclass      # decorator to set data class > 3.7
class Book:
    # attributes without default values have to come first
    title: str = "No Title"     # default value
    author: str = "No Author"     # default value
    pages: int = 0
    # price: float = field(default=float(10))     # via field
    price: float = field(default_factory=price_func)   # via function
    # price_func - calls method
    # price_func() - instantiate


b1 = Book("War and Peace", "Leo Tolstroy", 1225)
b2 = Book("The Cather in the Rye", "JD Salinger")
print(b1)
print(b2)
