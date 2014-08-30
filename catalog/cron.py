import os, webapp2, jinja2
from functions import BookLists

class UpdateBookLists(webapp2.RequestHandler):

    global bookLists
    bookLists = BookLists()

    def get(self):
        bookLists.update()
        self.response.write(bookLists.get_books_values())
