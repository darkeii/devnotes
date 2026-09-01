# Magic methods = Dunder methods (double underscore) __init__, __etr__, __eq__
#                 They arew automatically called by many of Python's built in operations.
#                 They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self, title, author, num_pages= 100):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):                            # lower than
        return self.num_pages < other.num_pages

    def __gt__(self, other):                            # greater than
        return self.num_pages > other.num_pages

    def __add__(self, other):                           # addition
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):                    # finds the keyword
        return keyword in self.title or keyword in self.author

    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "num_pages":
            return self.num_pages
        else:
            return f"{item} was not found"


book1 = Book("The Hobbit", "J.R.R Tolkien")
book2 = Book("Harry potter", "J.K Rolling", 223)
book3 = Book("The Lion , the witch and wardrobe", "C.S. Lewis", 172)
book4 = Book("Harry potter", "J.K Rolling", 170)

print(book1)
print(book2)
print(book3)


print(book2 == book4)               # It would still give false , even when everything is same, so lets define a new magic method

print(book2 < book4)

print(book1 + book2)

print("Lion" in book3)

print(book2['author'])



