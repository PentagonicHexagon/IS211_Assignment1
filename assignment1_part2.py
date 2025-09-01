#Work done by Samin Yasar
class Book:
    author = ""
    title = ""
    def __init__(self, author, title):
        self.author = author
        self.title = title
    def display(self):
        print(f"{self.title}, written by {self.author}")

book_I = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book_II = Book("Walter Scott", "Ivanhoe: A Romance")

book_I.display()
book_II.display()

