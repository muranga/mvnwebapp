import unittest
import webapp2

import main

class MainHandlerTest(unittest.TestCase):
    def test_hello(self):
	request = webapp2.Request.blank('/')
	response = request.get_response(main.app)
	self.assertEqual(response.status_int,200)
	self.assertTrue( 'Hello world' in response.body)

if __name__ == '__main__':
	unittest.main()
