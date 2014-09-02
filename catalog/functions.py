from time import time, clock
from credentials import email, password
from constants import BOOKS_OFFSET, BIG_BOOKS_OFFSET
import gspread

class BookLists:

    def __init__(self):
        start = clock()
        gc = gspread.login(email, password)
        spreadsheet = gc.open_by_key('1UCIE9Iy9xOjLQXSGON_1R40QldjjtRTsE5vGotZ0_vw')
        global books
        books = spreadsheet.worksheet("Book List")
        global big_books
        big_books = spreadsheet.worksheet("Big Book List")
        self.update()
        print "Initialized Book Lists in " + str(clock() - start) + " seconds."

    def update(self):
        global books_values
        books_values = books.get_all_values()[BOOKS_OFFSET:]
        global big_books_values
        big_books_values = big_books.get_all_values()[BIG_BOOKS_OFFSET:]

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

    def find_book_barcode(self, find_barcode):
        barcodes = bookLists.get_books_barcodes()
        i = 0
        while i < len(barcodes):
            if barcodes[i] != None:
                split_barcodes_by_comma = barcodes[i].replace(" ", "").split(',')
                for barcode in split_barcodes_by_comma:
                    if find_barcode == barcode:
                        return
            i += 1
