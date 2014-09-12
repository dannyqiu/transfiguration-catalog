import os, webapp2, jinja2
from catalog import JINJA_ENVIRONMENT, bookLists

class SearchForm(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render({}))

    def post(self):
        title = self.request.get('title')
        barcode = self.request.get('barcode')
        sticker = self.request.get('sticker')
        book_rows = []
        big_book_rows = []
        if title != "":
            book_titles = bookLists.get_books_titles()
            i = 0
            while i < len(book_titles):
                if title.lower() in book_titles[i].lower():
                    book_rows.append(i)
                i += 1
            book_titles = bookLists.get_big_books_titles()
            i = 0
            while i < len(book_titles):
                if title.lower() in book_titles[i].lower():
                    big_book_rows.append(i)
                i += 1
            search_query = title
        elif barcode != "":
            barcodes = bookLists.get_books_barcodes()
            i = 0
            while i < len(barcodes):
                if barcodes[i] != None:
                    split_barcodes_by_comma = barcodes[i].replace(" ", "").split(',')
                    for split_barcode in split_barcodes_by_comma:
                        if split_barcode == barcode:
                            book_rows.append(i)
                i += 1
            barcodes = bookLists.get_big_books_barcodes()
            i = 0
            while i < len(barcodes):
                if barcodes[i] != None:
                    split_barcodes_by_comma = barcodes[i].replace(" ", "").split(',')
                    for split_barcode in split_barcodes_by_comma:
                        if split_barcode == barcode:
                            big_book_rows.append(i)
                i += 1
            search_query = barcode
        elif sticker != "":
            stickers = bookLists.get_books_stickers()
            i = 0
            while i < len(stickers):
                if stickers[i] != None:
                    split_stickers_by_comma = stickers[i].replace(" ", "").split(',')
                    for split_sticker in split_stickers_by_comma:
                        if split_sticker.lower() == sticker.lower():
                            book_rows.append(i)
                i += 1
            stickers = bookLists.get_big_books_stickers()
            i = 0
            while i < len(stickers):
                if stickers[i] != None:
                    split_stickers_by_comma = stickers[i].replace(" ", "").split(',')
                    for split_sticker in split_stickers_by_comma:
                        if split_sticker.lower() == sticker.lower():
                            big_book_rows.append(i)
                i += 1
            search_query = sticker
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
        big_book_infos = []
        for big_book_row in big_book_rows:
            big_book_infos.append(bookLists.get_big_book_info(big_book_row))
        if len(book_infos) > 0 or len(big_book_infos) > 0:
            template_values = {
                'search_query': search_query,
                'books': book_infos,
                'big_books': big_book_infos
            }
            template = JINJA_ENVIRONMENT.get_template('search_completed.html')
        else:
            if title != "":
                error_message = "Title of <strong>" + title + "</strong> could not be found!"
            elif barcode != "":
                error_message = "Barcode of <strong>" + barcode + "</strong> could not be found!"
            elif sticker != "":
                error_message = "Sticker Tag of <strong>" + sticker + "</strong> could not be found!"
            template_values = {
                'error_message': error_message
            }
            template = JINJA_ENVIRONMENT.get_template('search_error.html')

        self.response.write(template.render(template_values))
