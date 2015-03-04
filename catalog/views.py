from cron import *
from catalog import *
from search import SearchForm
from borrow import BorrowForm
from returns import ReturnForm
from test import TestPage

class MainPage(BaseHandler):

    def get(self):
        self.render_template('index.html')

application = webapp2.WSGIApplication([
    ('/search', SearchForm),
    ('/borrow', BorrowForm),
    ('/return', ReturnForm),
    ('/test', TestPage),
    ('/tasks/update', UpdateBookLists),
    ('/.*', MainPage)
], debug=True)
