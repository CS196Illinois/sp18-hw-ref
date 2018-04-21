import unittest

# test file for homework 6

SMALL_TIMEOUT = 1

class tester_factorial(unittest.TestCase):

	@timeout_decorator.timeout(SMALL_TIMEOUT)
	def test__given(self):
		self.assertEqual(factorial(1), 1)
		self.assertEqual(factorial(2), 2)
		self.assertEqual(factorial(6), 720)


class tester_fibonacci(unittest.TestCase):
	
	@timeout_decorator.timeout(SMALL_TIMEOUT)
	def test__given(self):
		assert fibonacci(0) == 0
		assert fibonacci(8) == 21
		assert fibonacci(12) == 144
		assert fibonacci(21) == 10946

def lis(a):
	return longest_increasing_subsequence(a)

class tester_lis(unittest.TestCase):
	
	@timeout_decorator.timeout(SMALL_TIMEOUT)
	def test__given(self):
		self.assertEqual(lis([1,5,2,3]),3)

#===================================

# suppress stdout, but keep stderr since that's what unittest uses
# https://stackoverflow.com/questions/30715337

from io import StringIO
import sys

class ReplaceStd(object):
	""" Let's make it pythonic. """

	def __init__(self):
		self.stdout = None
		#self.stderr = None

	def __enter__(self):
		self.stdout = sys.stdout
		#self.stderr = sys.stderr

		# as it was suggested already:
		sys.stdout = StringIO()
		#sys.stderr = StringIO()

	def __exit__(self, type, value, traceback):
		sys.stdout.close()
		#sys.stderr.close()
		
		sys.stdout = self.stdout
		#sys.stderr = self.stderr

if __name__ == "__main__":
	
	with ReplaceStd():
		unittest.main(module=__name__, buffer=True, exit=False)
	
