from catalog import *
import gspread

def login():
    gc = gspread.login(email, password)
    spreadsheet = gc.open_by_key('1UCIE9Iy9xOjLQXSGON_1R40QldjjtRTsE5vGotZ0_vw')
    return spreadsheet

def get_books_barcodes():
    sheet = login().worksheet("Book List")
    barcodes = sheet.col_values(1)
    return barcodes

def get_books_stickers():
    sheet = login().worksheet("Book List")
    stickers = sheet.col_values(5)
    return stickers

def get_book_info(book_row):
    sheet = login().worksheet("Book List")
    information = sheet.row_values(book_row)
    return information

def get_big_books_barcodes():
    sheet = login().worksheet("Big Book List")
    barcodes = sheet.col_values(1)
    return barcodes

def get_big_books_stickers():
    sheet = login().worksheet("Big Book List")
    stickers = sheet.col_values(5)
    return stickers

def get_big_book_info(book_row):
    sheet = login().worksheet("Big Book List")
    information = sheet.row_values(book_row)
    return information

def get_books():
    return login().worksheet("Book List")

def get_books_spreadsheet():
    sheet = login().worksheet("Book List")
    return sheet.get_all_values()

def get_big_books_spreadsheet():
    sheet = login().worksheet("Big Book List")
    return sheet.get_all_values()
