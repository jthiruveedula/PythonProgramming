from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass


# Write MyBook class

class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.price)


# title=input()
# author=input()
# price=int(input())


new_novel = MyBook('The Alchemist', 'Paulo Coelho', '248')
new_novel.display()

# output
# Title: The
# Alchemist
# Author: Paulo
# Coelho
# Price: 248
