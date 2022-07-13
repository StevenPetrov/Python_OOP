class Book:
    def __init__(self, name=None, author=None, pages=None,):
        self.name = name
        self.author = author
        self.pages = pages

book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
