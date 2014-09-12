import os, webapp2, jinja2, time
from catalog import JINJA_ENVIRONMENT, bookLists
from constants import BOOKS_OFFSET, BIG_BOOKS_OFFSET

from google.appengine.api import users

class ReturnForm(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('return.html')
        self.response.write(template.render({}))

    def post(self):
        user_logged_in = users.get_current_user()
        contact = user_logged_in.nickname() + ":" + user_logged_in.email()
        borrowed_barcodes = self.request.get('barcodes')
        borrowed_barcodes = borrowed_barcodes.split('\r\n')
        borrowed_barcodes = filter(lambda b: b != "", borrowed_barcodes) # Take out all empty barcodes
        borrowed_stickers = self.request.get('stickers')
        borrowed_stickers = borrowed_stickers.split('\r\n')
        borrowed_stickers = filter(lambda t: t != "", borrowed_stickers)

        error_barcodes = []
        error_stickers = []
        book_rows = []
        book_infos = []
        if self.request.get('book_type') == "Big Book":
            barcodes = bookLists.get_big_books_barcodes()
            for borrowed_barcode in borrowed_barcodes:
                i = 0
                book_found = False
                while i < len(barcodes) and book_found == False:
                    split_barcodes_by_comma = barcodes[i].split(',')
                    for split_barcode in split_barcodes_by_comma:
                        if borrowed_barcode in split_barcode:
                            book_rows.append(i)
                            book_found = True
                            break
                    i += 1
                if not book_found:
                    error_barcodes.append(borrowed_barcode)
            stickers = bookLists.get_big_books_stickers()
            for borrowed_sticker in borrowed_stickers:
                i = 0
                book_found = False
                while i < len(stickers) and book_found == False:
                    split_stickers_by_comma = stickers[i].split(',')
                    for split_sticker in split_stickers_by_comma:
                        if borrowed_sticker in split_sticker:
                            book_rows.append(i)
                            book_found = True
                            break
                    i += 1
                if not book_found:
                    error_stickers.append(borrowed_sticker)
            books = bookLists.get_big_books()
            for book_row in book_rows:
                original_borrowers = books.cell(book_row + BIG_BOOKS_OFFSET + 1, 7).value
                borrowers = original_borrowers.split("\n")
                i = 0
                while i < len(borrowers):
                    if contact in borrowers[i]:
                        break
                    i += 1
                if i == len(borrowers):
                    error_barcodes.append(barcodes[book_row])
                else:
                    borrowers.pop(i)
                    new_borrowers = "\n".join(borrowers)
                    books.update_cell(book_row + BIG_BOOKS_OFFSET + 1, 7,new_borrowers)
                    book_infos.append(bookLists.get_big_book_info(book_row))
        else:
            barcodes = bookLists.get_books_barcodes()
            for borrowed_barcode in borrowed_barcodes:
                i = 0
                book_found = False
                while i < len(barcodes) and book_found == False:
                    split_barcodes_by_comma = barcodes[i].split(',')
                    for split_barcode in split_barcodes_by_comma:
                        if borrowed_barcode in split_barcode:
                            book_rows.append(i)
                            book_found = True
                            break
                    i += 1
                if not book_found:
                    error_barcodes.append(borrowed_barcode)
            stickers = bookLists.get_books_stickers()
            for borrowed_sticker in borrowed_stickers:
                i = 0
                book_found = False
                while i < len(stickers) and book_found == False:
                    split_stickers_by_comma = stickers[i].split(',')
                    for split_sticker in split_stickers_by_comma:
                        if borrowed_sticker in split_sticker:
                            book_rows.append(i)
                            book_found = True
                            break
                    i += 1
                if not book_found:
                    error_stickers.append(borrowed_sticker)
            books = bookLists.get_books()
            for book_row in book_rows:
                original_borrowers = books.cell(book_row + BOOKS_OFFSET + 1, 7).value
                borrowers = original_borrowers.split("\n")
                i = 0
                while i < len(borrowers):
                    if contact in borrowers[i]:
                        break
                    i += 1
                if i == len(borrowers):
                    error_barcodes.append(barcodes[book_row])
                else:
                    borrowers.pop(i)
                    new_borrowers = "\n".join(borrowers)
                    books.update_cell(book_row + BOOKS_OFFSET + 1, 7,new_borrowers)
                    book_infos.append(bookLists.big_book_info(book_row))

        template_values = {
            'contact': contact,
            'books': book_infos,
            'errors': error_barcodes
        }

        template = JINJA_ENVIRONMENT.get_template('return_completed.html')
        self.response.write(template.render(template_values))