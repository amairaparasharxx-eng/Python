class book:
    def __init__(self, title, author, is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def borrow(self):
        self.is_borrowed=True
    def return_book(self):
        self.is_borrowed=False
    def details(self):
        print("Title: ",self.title)
        print("Author: ",self.author)

b1=book("Harry Potter: Chamber of Secrets","JK Rowling")
b1.details()
b1.borrow()
print("Book 1: Borrowed Status: ",b1.is_borrowed)
b1.return_book()
print("Book 1:Borrowed Status: ",b1.is_borrowed)
print()

b2=book("The Hunger Games","Suzanne Collins")
b2.details()
b2.borrow()
print("Book 2: Borrowed Status: ",b2.is_borrowed)
b2.return_book()
print("Book 2: Borrowed Status: ",b2.is_borrowed)
print()

b3=book("BFG","Roald Dahl")
b3.details()
b3.borrow()
print("Book 3: Borrowed Status: ",b3.is_borrowed)
b3.return_book()
print("Book 3: Borrowed Status: ",b3.is_borrowed)
print()