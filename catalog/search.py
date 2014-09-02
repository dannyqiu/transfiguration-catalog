import os, webapp2, jinja2
from catalog import JINJA_ENVIRONMENT, bookLists

class SearchForm(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render({}))

    def post(self):
        title = self.request.get('title')
        barcode = self.request.get('barcode')
        tag = self.request.get('sticker')
        book_rows = []
        if title != "":
            book_titles = bookLists.get_books_titles()
            i = 0
            while i < len(book_titles):
                if title in book_titles[i]:
                    book_rows.append(i)
                i += 1
        elif barcode != "":
            try:
                book_rows.append(bookLists.get_books_barcodes().index(barcode))
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
                            book_rows.append(i)
                i += 1
        else:
            template_values = {
                'error_message': "Nothing to search for!"
            }
            template = JINJA_ENVIRONMENT.get_template('search_error.html')
            self.response.write(template.render(template_values))
            return

        book_infos = []
        for book_row in book_rows:
            book_infos.append(bookLists.get_book_info(book_row))
        if len(book_infos) > 0:
            template_values = {
                'books': book_infos
            }
            template = JINJA_ENVIRONMENT.get_template('search_completed.html')
        else:
            if title != "":
                error_message = "Title of <strong>" + title + "</strong> could not be found!"
            elif barcode != "":
                error_message = "Barcode of <strong>" + barcode + "</strong> could not be found!"
            elif tag != "":
                error_message = "Sticker Tag of <strong>" + tag + "</strong> could not be found!"
            template_values = {
                'error_message': error_message
            }
            template = JINJA_ENVIRONMENT.get_template('search_error.html')

        self.response.write(template.render(template_values))
