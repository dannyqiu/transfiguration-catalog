import os, webapp2, jinja2
from catalog import *

class TestPage(webapp2.RequestHandler):

    def get(self):
        books = bookLists.get_books_values()
        books = [[books[r][c] for c in [0,1,2,3,4,6]] for r in range(0,len(books))]
        big_books = bookLists.get_big_books_values()
        big_books = [[big_books[r][c] for c in [0,1,2,3,4,6]] for r in range(0,len(big_books))]

        template_values = {
            'books': books,
            'big_books': big_books
        }
        render_template(self, 'test.html', template_values)
