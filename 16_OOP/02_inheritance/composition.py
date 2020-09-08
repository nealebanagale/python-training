# composition - we build objects out of other objects
#             - this model is more of a has relationship.
class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        # monolithic class definition - should be separate entities
        # self.authorfname = authorfname
        # self.authorlname = authorlname
        self.author = author    # book has author vs book has author details
        self.chapters = []

    # def addchapter(self, name, pages):
    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # string method
    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


# b1 = Book("War and Peace", 39.0, "Leo", "Tolstroy")
author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, author)
b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))
print(b1.title)
print(b1.author)
print(b1.getbookpagecount())
