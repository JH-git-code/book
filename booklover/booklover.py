class BookLover:
    import pandas as pd
    import numpy as np
    
    name = ''
    email = ''
    fav_genre = ''
    num_books = 0
    book_list = pd.DataFrame({'book_name':[],'book_rating':[]})
    
    def __init__(self, name, email, fav_genre, num_books = num_books, book_list = book_list):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        import pandas as pd
        newBook = pd.DataFrame({'book_name':[book_name],'book_rating':[rating]})
        if self.has_read(book_name) == False:
            self.book_list = pd.concat([self.book_list, newBook], ignore_index=True)
        
        
    def has_read(self, book_name):
        import pandas as pd
        test = self.book_list[self.book_list.book_name == book_name].copy()
        if len(test) != 0:
            return True
        else:
            return False
         
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):     
        return self.book_list[self.book_list.book_rating > 3].copy()
    
    
        