import unittest
from greeter import greeter

class GreeterTest(unittest.TestCase):

	def test_empty_string(self):
		self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

	def test_not_string_inputs(self):
		self.assertFalse(greeter(123))

	def test_extra_long_string(self):
		long_name = 'Peeeeti' * 100
		self.assertEqual(greeter(long_name), 'Hello, ' + long_name + '!')

if __name__ == '__main__':
	unittest.main()