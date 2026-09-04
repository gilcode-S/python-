

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


book1 = Book("The hobbit", "J.r.r", 310)
book2 = Book("The hobbit 2", "J.r.r", 313)
book3 = Book("The hobbit 3", "J.r.r", 413)

print(book2 == book3)
