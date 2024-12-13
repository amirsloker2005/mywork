class Book:
    def __init__(self, title : str, author : str, publication_year : int, is_borrowed : bool):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = is_borrowed

    def borrow(self):
        self.is_borrowed = True

    def Return(self):
        self.is_borrowed = False
