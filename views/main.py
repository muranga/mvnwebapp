import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),"..","templates")),
    extensions=['jinja2.ext.autoescape'])

class CustomHandler(webapp2.RequestHandler):
    def render_template(self,name,data):
	template = JINJA_ENVIRONMENT.get_template(name)
	self.response.write(template.render(data))

class MainHandler(CustomHandler):
    def get(self):
	self.render_template('index.html',{})
