import time
from functools import wraps

def excecution_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'\n[LOG] Starting execution of {func.__name__}...')
        result = func(*args, **kwargs)
        print(f'[LOG] Finished execution of {func.__name__}.')
        return result 
    return wrapper

class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Book(Item):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn

class Library:
    def __init__(self):
        self.book = []

    @excecution_log
    def add_book(self, book_obj):
        self.book.append(book_obj)
        print(f'Book "{book_obj.title}" added to the library.')
    
    def get_book_generator(self):
        for book in self.book:
            yield f'Title: {book.title}, Author: {book.author}, Available: {book.is_available}'

    def show_books(self):
        available_books = [b.title for b in self.book if b.is_available]
        if not available_books:
            print('No books available in the library.')
            return  
        else:
            print(f'Available books in the library: {", ".join(available_books)}')
            

def main():
    my_library = Library()

    book1 = Book('1984', 'George Orwell', '1234567890')
    book2 = Book('To Kill a Mockingbird', 'Harper Lee', '0987654321')

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.show_books()

    while True:
        print('\nLibrary Menu:')
        print('1. View all books')
        print('2. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            for book_info in my_library.get_book_generator():
                print(book_info)
        elif choice == '2':
            print('Exiting the library system. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()