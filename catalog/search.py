import os, webapp2, jinja2
from catalog import JINJA_ENVIRONMENT
from functions import BookLists

class SearchForm(webapp2.RequestHandler):

    global bookLists
    bookLists = BookLists()

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render({}))

    def post(self):
        barcode = self.request.get('barcode')
        tag = self.request.get('sticker')
        if barcode != "":
            try:
                book_row = bookLists.get_books_barcodes().index(barcode)
            except:
                pass
        elif tag != "":
            stickers = bookLists.get_books_stickers()
            i = 0
            while i < len(stickers):
                if stickers[i] != None:
                    split_stickers_by_comma = stickers[i].split(',')
                    for sticker in split_stickers_by_comma:
                        if tag == sticker:
                            book_row = i
                            break
                i += 1
        else:
            self.response.write("Nothing to search for!")
            return

        try:
            book_info = bookLists.get_book_info(book_row)
            template_values = {
                'barcode': book_info[0],
                'title': book_info[1],
                'author': book_info[2],
                'quantity': book_info[3],
                'sticker': book_info[4]
            }
            template = JINJA_ENVIRONMENT.get_template('search_completed.html')
        except:
            if barcode != "":
                error_message = "Barcode of <strong>" + barcode + "</strong> could not be found!"
            elif tag != "":
                error_message = "Sticker Tag of <strong>" + tag + "</strong> could not be found!"
            template_values = {
                'error_message': error_message
            }
            template = JINJA_ENVIRONMENT.get_template('search_error.html')

        self.response.write(template.render(template_values))
