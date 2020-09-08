class Book:
    def __init__(self, title):
        self.title = title


class NewsPaper:
    def __init__(self, name):
        self.name = name


b1 = Book("the Cather In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = NewsPaper("The Washingon Post")
n2 = NewsPaper("The New York Times")

# type()
print(type(b1))
print(type(n1))
# best for comparing types
print(type(b1) == type(b2))
print(type(b1) == type(n1))

# isinstance()
# best for comparing know types
print(isinstance(b1, Book))
print(isinstance(n1, NewsPaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))   # built in object class
