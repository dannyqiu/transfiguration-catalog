import webapp2, jinja2
from catalog import *

class UpdateBookLists(webapp2.RequestHandler):

    def get(self):
        bookLists.update()
        self.response.write(bookLists.get_books_values())
