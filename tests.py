import unittest
import webapp2

import main

class MainHandlerTest(unittest.TestCase):
    def test_hello(self):
	request = webapp2.Request.blank('/')
	response = request.get_response(main.app)
	self.assertEqual(response.status_int,200)
	self.assertEqual(response.body, 'Hello world!')

if __name__ == '__main__':
	unittest.main()
