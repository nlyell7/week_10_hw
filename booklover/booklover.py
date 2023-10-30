import pandas as pd

class BookLover:

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        self.book_list = book_list

    def add_book(self, book_name, rating):
        if (book_name in self.book_list.values):
            print("This book has already been rated")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books = self.num_books + 1

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]  

if __name__ == '__main__':     
    booklover1 = BookLover('Seth', 'nth@ghail', 'Fantasy')
    booklover1.add_book('Fellowship of the ring', 5)
    booklover1.add_book('The Two Towers', 4)
    booklover1.add_book('The Return of the King', 5)
    booklover1.add_book('Frames for Undergraduates', 2)
    booklover1.add_book('Wild at Heart', 2)

    new_list = booklover1.fav_books()
    print(new_list)

    for i in range(0,len(new_list)):
        print(new_list['book_rating'][i])   

    print(booklover1.has_read('The Two Towers'))
    print(booklover1.book_list['book_name'])
    book = "The Two Towers"
    print(book in booklover1.book_list['book_name'].values)


