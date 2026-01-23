class Book:
    library_name = "Python Library"

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"title {self.title} by {self.author} "


book1 = Book("Python", "cj")
book2 = Book("CS", "jc")

print(book1)
print(book2)
