import os, webapp2, jinja2, time
from constants import *
from functions import BookLists

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'])

os.environ['TZ'] = TIMEZONE

global bookLists
bookLists = BookLists()
