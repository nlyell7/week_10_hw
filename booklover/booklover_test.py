import unittest

import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        booklover1 = BookLover('Seth', 'nth@ghail', 'Fantasy')
        # add a book and test if it is in `book_list`.
        booklover1.add_book('Fellowship of the Ring', 5)
        book = 'Fellowship of the Ring'
        print(booklover1.book_list)
        self.assertTrue(book in booklover1.book_list.values)

    def test_2_add_book(self):
        booklover1 = BookLover('Seth', 'nth@ghail', 'Fantasy')
        # add the same book twice. Test if it's in `book_list` only once.
        booklover1.add_book('Fellowship of the ring', 5)
        booklover1.add_book('Fellowship of the ring', 5)
        self.assertEquals(len(booklover1.book_list['book_name']),1)
       
                
    def test_3_has_read(self): 
        booklover1 = BookLover('Seth', 'nth@ghail', 'Fantasy')
        # pass a book in the list and test if the answer is `True`.
        booklover1.add_book('Fellowship of the Ring', 5)
        self.assertTrue(booklover1.has_read('Fellowship of the Ring'))
        
    def test_4_has_read(self): 
        booklover1 = BookLover('Seth', 'nth@ghail', 'Fantasy')
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        self.assertFalse(booklover1.has_read('The Two Towers'))
        
    def test_5_num_books_read(self): 
        booklover1 = BookLover('Seth', 'nth@ghail', 'Fantasy')
        # add some books to the list, and test num_books matches expected.
        booklover1.add_book('Fellowship of the ring', 5)
        booklover1.add_book('The Two Towers', 4)
        booklover1.add_book('The Return of the King', 5)

        self.assertEqual(len(booklover1.book_list),3)


    def test_6_fav_books(self):
        booklover1 = BookLover('Seth', 'nth@ghail', 'Fantasy')
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover1.add_book('Fellowship of the ring', 5)
        booklover1.add_book('The Two Towers', 4)
        booklover1.add_book('The Return of the King', 5)
        booklover1.add_book('Frames for Undergraduates', 2)
        booklover1.add_book('Wild at Heart', 3)

        new_list = booklover1.fav_books()
        
        for i in range(1,len(new_list)):
            self.assertGreater(new_list['book_rating'][i],3)

        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)