import os, webapp2, jinja2
from functions import BookLists
from cron import *
from catalog import JINJA_ENVIRONMENT
from search import SearchForm
from borrow import BorrowForm

class MainPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))

class TestPage(webapp2.RequestHandler):

    global bookLists
    bookLists = BookLists()

    def get(self):
        template_values = {
            'barcodes': bookLists.get_books_barcodes(),
            'big_book_barcodes': bookLists.get_big_books_barcodes()
            #'barcodes': get_books_spreadsheet(),
            #'big_book_barcodes': get_big_books_spreadsheet()
        }
        template = JINJA_ENVIRONMENT.get_template('test.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/search', SearchForm),
    ('/borrow', BorrowForm),
    ('/test', TestPage),
    ('/tasks/update', UpdateBookLists),
    ('/.*', MainPage)
], debug=True)
