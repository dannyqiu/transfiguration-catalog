import os, webapp2, jinja2
from catalog import JINJA_ENVIRONMENT
from functions import BookLists

class TestPage(webapp2.RequestHandler):

    global bookLists
    bookLists = BookLists()

    def get(self):
        books = bookLists.get_books_values()
        books = [[books[r][c] for c in range(0,5)] for r in range(0,len(books))]
        big_books = bookLists.get_big_books_values()
        big_books = [[big_books[r][c] for c in range(0,5)] for r in range(0,len(big_books))]

        template_values = {
            'books': books,
            'big_books': big_books
        }
        template = JINJA_ENVIRONMENT.get_template('test.html')
        self.response.write(template.render(template_values))
