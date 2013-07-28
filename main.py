#!/usr/bin/env python
import webapp2
from views.main import MainHandler
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
