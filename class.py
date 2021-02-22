#!/usr/bin/python

# Very simple example showing how to use a class
# Expand on this as needed

class Book:
    def __init__(self,title,price=0.0):
        self.title = title
        self.price = price
        self.text  = ""

DATA = {}
aBook = Book("First Book",99.00)
DATA["1"] = aBook
DATA["2"] = Book("Second Book", 55.10)
DATA["2"].text = "this is text"
DATA["1"].anArray = []
DATA["1"].anArray.append("One")
DATA["1"].anArray.append("Two")

print DATA["1"].title, DATA["2"].title
print DATA["2"].text

DATA["2"].text = "this is text 2"

print "data.2.text: ", DATA["2"].text
print "anArray: ", DATA["1"].anArray

# Put in a list
bookList = []
bookList.append(Book("First Book", 14.99))
aBook = Book("Second Book", 99.00)
bookList.append(aBook)

for book in bookList:
    print book.title, " | ", book.price

