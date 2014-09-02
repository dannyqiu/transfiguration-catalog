import os, webapp2, jinja2
from cron import *
from catalog import JINJA_ENVIRONMENT, bookLists
from search import SearchForm
from borrow import BorrowForm
from test import TestPage

class MainPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))

application = webapp2.WSGIApplication([
    ('/search', SearchForm),
    ('/borrow', BorrowForm),
    ('/test', TestPage),
    ('/tasks/update', UpdateBookLists),
    ('/.*', MainPage)
], debug=True)
