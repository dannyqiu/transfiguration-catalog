import os, webapp2, jinja2, datetime
from catalog import JINJA_ENVIRONMENT
from functions import BookLists

class BorrowForm(webapp2.RequestHandler):

    global bookLists
    bookLists = BookLists()

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('borrow.html')
        self.response.write(template.render({}))

    def post(self):
        contact = self.request.get('contact')
        borrowed_barcodes = self.request.get('barcode')
        borrowed_barcodes = borrowed_barcodes.split('\r\n')

        if self.request.get('book_type') == "Big Book":
            barcodes = bookLists.get_big_books_barcodes()
            book_rows = []
            error_barcodes = []
            for borrowed_barcode in borrowed_barcodes:
                try:
                    book_rows.append(barcodes.index(borrowed_barcode))
                except:
                    error_barcodes.append(borrowed_barcode)
            book_infos = []
            books = bookLists.get_big_books()
            for book_row in book_rows:
                original_borrower = books.cell(book_row + 1, 7).value
                books.update_cell(book_row + 1, 7, original_borrower + "\n" + str(datetime.datetime.now()) + " - " + contact)
                book_infos.append(bookLists.get_big_book_info(book_row))

        else:
            barcodes = bookLists.get_books_barcodes()
            book_rows = []
            error_barcodes = []
            for borrowed_barcode in borrowed_barcodes:
                try:
                    book_rows.append(barcodes.index(borrowed_barcode))
                except:
                    error_barcodes.append(borrowed_barcode)
            book_infos = []
            books = bookLists.get_books()
            for book_row in book_rows:
                original_borrower = books.cell(book_row + 1, 7).value
                books.update_cell(book_row + 1, 7, original_borrower + "\n" + str(datetime.datetime.now()) + " - " + contact)
                book_infos.append(bookLists.get_book_info(book_row))
        
        template_values = {
            'contact': contact,
            'books': book_infos,
            'errors': error_barcodes
        }

        template = JINJA_ENVIRONMENT.get_template('borrow_completed.html')
        self.response.write(template.render(template_values))
