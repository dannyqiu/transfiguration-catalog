from time import time
from catalog import email, password
import gspread

class BookLists:

    def __init__(self):
        gc = gspread.login(email, password)
        spreadsheet = gc.open_by_key('1UCIE9Iy9xOjLQXSGON_1R40QldjjtRTsE5vGotZ0_vw')
        global books
        books = spreadsheet.worksheet("Book List")
        global big_books
        big_books = spreadsheet.worksheet("Big Book List")
        self.update()

    def get_books(self):
        return books

    def get_books_values(self):
        return books_values

    def get_books_barcodes(self):
        barcodes = []
        for row in books_values:
            barcodes.append(row[0])
        return barcodes

    def get_books_titles(self):
        titles = []
        for row in books_values:
            titles.append(row[1])
        return titles

    def get_books_stickers(self):
        stickers = []
        for row in books_values:
            stickers.append(row[4])
        return stickers

    def get_book_info(self, book_row):
        return books_values[book_row]

    def get_big_books(self):
        return big_books

    def get_big_books_values(self):
        return big_books_values

    def get_big_books_barcodes(self):
        barcodes = []
        for row in big_books_values:
            barcodes.append(row[0])
        return barcodes

    def get_big_books_titles(self):
        titles = []
        for row in big_books_values:
            titles.append(row[1])
        return titles

    def get_big_books_stickers(self):
        stickers = []
        for row in big_books_values:
            stickers.append(row[4])
        return stickers

    def get_big_book_info(self, book_row):
        return big_books_values[book_row]

    def update(self):
        global books_values
        books_values = books.get_all_values()[10:]
        global big_books_balues
        big_books_values = big_books.get_all_values()[1:]
