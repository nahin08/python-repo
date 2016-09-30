
from sys import argv
from simple_download import simple_downloder
import unittest
	
class MyTest(unittest.TestCase):

	def test_input_file(self):
		self.assertEqual(simple_downloder("url01.txt"), 5)
		
	def test_empty_input_file(self):
		self.assertEqual(simple_downloder("url02.txt"), 0)
		
	def test_invalid_url(self):
		self.assertEqual(simple_downloder("url03.txt"), 0)

	def test_invalid_filename(self):
		self.assertEqual(simple_downloder("url04.txt"), 0)		

		
if __name__ == '__main__':	
    unittest.main()