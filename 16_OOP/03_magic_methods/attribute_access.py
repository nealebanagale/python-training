class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    #
    # # directly access the attribute name, otherwise recursive loop is created
    # # additional code handling can be added
    # def __getattribute__(self, name):
    #     if name == "price":
    #         # call current value from super()
    #         p = super().__getattribute__("price")
    #         d = super().__getattribute__("_discount")
    #         return p - (p * d)
    #     return super().__getattribute__(name)

    # setting of attribute
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name, value)

    # __getattr version of __getattribute / lookup fails
    # triggers when no __getattribute, throws exception, attribute not exist
    def __getattr__(self, name):
        return name + "is not here!"


b1 = Book("War and Peace", "Leo Tolstroy", 39.0)
b2 = Book("The Cather in the Rye", "JD Salinger", 29.95)


b1.price = 38.95
print(b1)       # triggers __getattribute

# triggers __getattribute
b2.price = float(40)
print(b2)

print(b1.randomprop)
