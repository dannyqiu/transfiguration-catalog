import sys, os, logging, json
from time import time, clock
import gspread
from oauth2client.client import GoogleCredentials
from constants import *

def trim_list_end(book_list):
    i = len(book_list)
    while i > 0:
        i -= 1
        book_row = book_list[i]
        if book_row[0].strip() != "" or book_row[1].strip() != "" or book_row[4].strip() != "": # Remove element if barcode, title and sticker don't exist
            break
    return book_list[:i+1]

class BookLists:

    def __init__(self):
        global books
        global big_books
        global audio_books
        global books_values
        global big_books_values
        global audo_books_values
        global updated_book_time
        global updated_big_book_time
        global updated_audio_book_time
        books = None
        books_values = None
        big_books = None
        big_books_values = None
        audio_books = None
        audio_books_values = None
        updated_book_time = "Not Initialized"
        updated_big_book_time = "Not Initialized"
        updated_audio_book_time = "Not Initialized"
        self.update()

    def login(self):
        if os.environ.has_key('GOOGLE_APPLICATION_CREDENTIALS'):
            logging.info("Logging in with credentials located at " + os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
        else:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json')
            logging.info("Google is bugging out! We have to set the GOOGLE_APPLICATION_CREDENTIALS environment variable again... " + os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = GoogleCredentials.get_application_default()
        credentials = credentials.create_scoped(scope)
        gs = gspread.authorize(credentials)
        spreadsheet = gs.open_by_key(SPREADSHEET_KEY)
        return spreadsheet

    def update(self):
        start = clock()
        spreadsheet = self.login()
        global books
        global big_books
        global audio_books
        while True: # Hack to continue retrying to update cell
            try:
                books = spreadsheet.worksheet("Book List")
            except Exception:
                continue
            break
        while True: # Hack to continue retrying to update cell
            try:
                big_books = spreadsheet.worksheet("Big Book List")
            except Exception:
                continue
            break
        while True: # Hack to continue retrying to update cell
            try:
                audio_books = spreadsheet.worksheet("Audiobooks in Ziplock Bags")
            except Exception:
                continue
            break

        global books_values
        global big_books_values
        global audio_books_values
        global updated_book_time
        global updated_big_book_time
        global updated_audio_book_time
        if books.updated != updated_book_time:
            logging.info("Books update time: " + updated_book_time)
            while True: # Hack to continue retrying to update cell
                try:
                    books_values = books.get_all_values()[BOOKS_OFFSET:]
                except Exception:
                    continue
                break
            books_values = trim_list_end(books_values)
            updated_book_time = books.updated
        if big_books.updated != updated_big_book_time:
            logging.info("Big books update time: " + updated_big_book_time)
            while True: # Hack to continue retrying to update cell
                try:
                    big_books_values = big_books.get_all_values()[BIG_BOOKS_OFFSET:]
                except Exception:
                    continue
                break
            big_books_values = trim_list_end(big_books_values)
            updated_big_book_time = big_books.updated
        if audio_books.updated != updated_audio_book_time:
            logging.info("Audio books update time: " + updated_audio_book_time)
            while True: # Hack to continue retrying to update cell
                try:
                    audio_books_values = audio_books.get_all_values()[AUDIO_BOOKS_OFFSET:]
                except Exception:
                    continue
                break
            audio_books_values = trim_list_end(audio_books_values)
            updated_audio_book_time = audio_books.updated
        logging.info("Initialized Book Lists in " + str(clock() - start) + " seconds.")

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

    def get_audio_books(self):
        return audio_books

    def get_audio_books_values(self):
        return audio_books_values

    def get_audio_books_barcodes(self):
        barcodes = []
        for row in audio_books_values:
            barcodes.append(row[0])
        return barcodes

    def get_audio_books_titles(self):
        titles = []
        for row in audio_books_values:
            titles.append(row[1])
        return titles

    def get_audio_books_stickers(self):
        stickers = []
        for row in audio_books_values:
            stickers.append(row[4])
        return stickers

    def get_audio_book_info(self, book_row):
        return audio_books_values[book_row]
