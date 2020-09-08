class Book:
    # overrides built in init function
    # init - initializer, and not constructor (obj is created when its called)
    # self - the object itself gets automatically passed in as the 1st argument
    def __init__(self, title):
        self.title = title


b1 = Book("Brave new book")
b2 = Book("War and Peace")
print(b1.title)
print(b2.title)
