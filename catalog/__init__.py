import os, webapp2, jinja2
from google.appengine.api import users
from constants import *
from functions import BookLists

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'])

global bookLists
bookLists = BookLists()

class BaseHandler(webapp2.RequestHandler):

    def render_template(self, template_filename, template_values={}):
        user = users.get_current_user()
        if user:
            template_values['user'] = user.email()
            template_values['logout_url'] = users.create_logout_url('/')
        template = JINJA_ENVIRONMENT.get_template(template_filename)
        self.response.out.write(template.render(template_values))
