import os, webapp2, jinja2
from functions import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))

class SearchForm(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render({}))

    def post(self):
        barcode = self.request.get('barcode')
        tag = self.request.get('sticker')
        if barcode != "":
            book_row = get_books_barcodes().index(barcode) + 1
        elif tag != "":
            stickers = get_books_stickers()
            i = 0
            while i < len(stickers):
                if stickers[i] != None:
                    split_stickers_by_comma = stickers[i].split(',')
                    for sticker in split_stickers_by_comma:
                        if tag == sticker:
                            book_row = i + 1
                i += 1
        else:
            self.response.write("Nothing to search for!")
            return

        book_info = get_book_info(book_row)

        template_values = {
            'barcode': book_info[0],
            'title': book_info[1],
            'author': book_info[2],
            'quantity': book_info[3],
            'sticker': book_info[4],
        }

        template = JINJA_ENVIRONMENT.get_template('search_completed.html')
        self.response.write(template.render(template_values))

class BorrowForm(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('borrow.html')
        self.response.write(template.render({}))

    def post(self):
        contact = self.request.get('contact')
        borrowed_barcodes = self.request.get('barcode')
        borrowed_barcodes = borrowed_barcodes.split('\r\n')
        barcodes = get_books_barcodes()
        book_rows = []
        error_barcodes = []
        for borrowed_barcode in borrowed_barcodes:
            try:
                book_rows.append(barcodes.index(borrowed_barcode) + 1)
            except:
                error_barcodes.append(borrowed_barcode)
        book_infos = []
        books = get_books()
        for book_row in book_rows:
            books.update_cell(book_row, 7, contact)
            book_infos.append(get_book_info(book_row))
        
        template_values = {
            'contact': contact,
            'books': book_infos,
            'errors': error_barcodes
        }

        template = JINJA_ENVIRONMENT.get_template('borrow_completed.html')
        self.response.write(template.render(template_values))

class TestPage(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'barcodes': get_books_barcodes(),
            'big_book_barcodes': get_big_books_barcodes()
            #'barcodes': get_books_spreadsheet(),
            #'big_book_barcodes': get_big_books_spreadsheet()
        }
        template = JINJA_ENVIRONMENT.get_template('test.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/search', SearchForm),
    ('/borrow', BorrowForm),
    ('/test', TestPage),
    ('/.*', MainPage)
], debug=True)
