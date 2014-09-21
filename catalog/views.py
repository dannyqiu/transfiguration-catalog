import os, webapp2, jinja2
from cron import *
from catalog import *
from search import SearchForm
from borrow import BorrowForm
from returns import ReturnForm
from test import TestPage

class MainPage(webapp2.RequestHandler):

    def get(self):
        render_template(self, 'index.html')

application = webapp2.WSGIApplication([
    ('/search', SearchForm),
    ('/borrow', BorrowForm),
    ('/return', ReturnForm),
    ('/test', TestPage),
    ('/tasks/update', UpdateBookLists),
    ('/.*', MainPage)
], debug=True)
