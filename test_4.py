import unittest
from greeter import greeter

class GreeterTest(unittest.TestCase):

	def test_empty_string(self):
		self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

	def test_extra_long_string(self):
		long_name = 'Peeeeti' * 100
		self.assertEqual(greeter(long_name), 'Hello, ' + long_name + '!')

	def test_with_name(self):
		self.assertEqual(greeter('Peter'), 'Hello, Peter!')

	def test_with_digit_name(self):
		self.assertEqual(greeter('P3t3r'), 'Hello, P3t3r!')

	def test_with_uppercase_name(self):
		self.assertEqual(greeter('PETER'), 'Hello, PETER!')

if __name__ == '__main__':
	unittest.main()