import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        booklover1 = BookLover('Tom','tom@uva.com', 'Hist')
        booklover1.add_book('LOTR', 5)
        self.assertEqual(len(booklover1.book_list), 1)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover2 = BookLover('Tom','tom@uva.com', 'Hist')
        booklover2.add_book('LOTR', 5)
        booklover2.add_book('LOTR', 4)
        self.assertEqual(len(booklover2.book_list), 1)
        
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        booklover3 = BookLover('Tom','tom@uva.com', 'Hist')
        booklover3.add_book('LOTR', 5)
        self.assertTrue(booklover3.has_read('LOTR'))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover4 = BookLover('Tom','tom@uva.com', 'Hist')
        self.assertFalse(booklover4.has_read('LOTR'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        booklover5 = BookLover('Tom','tom@uva.com', 'Hist')
        booklover5.add_book('LOTR', 5)
        booklover5.add_book('LOTR', 5)
        booklover5.add_book('CAT', 4)
        booklover5.add_book('DOG', 3)
        self.assertEqual(booklover5.num_books_read(),3)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover6 = BookLover('Tom','tom@uva.com', 'Hist')
        booklover6.add_book('LOTR', 5)
        booklover6.add_book('CAT', 4)
        booklover6.add_book('DOG', 3)
        booklover6.add_book('COW', 2)
        booklover6.add_book('MOOSE', 1)
        self.assertEqual(len(booklover6.fav_books()), 2)
    
if __name__ == '__main__':
    
    unittest.main(verbosity=3)