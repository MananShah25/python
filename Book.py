class Book:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author

    def display(self):
        print("Title: "+self.__title)
        print("Author: "+self.__author)


PP = Book("Pride and Prejudice","Jane Austen")
H = Book("Hamlet","William Shakespeare")
WP = Book("War and Peace","Leo Tolstoy")

HP = Book("Harry Potter","J.K. Rowling")

PP.display()
H.display()
WP.display()
HP.display()
