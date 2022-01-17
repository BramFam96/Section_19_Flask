from unittest import TestCase
from algos import reverse_str, is_palindrome, factorial;

class AlgoTestCase(TestCase):
  def test_reverse_str(self):
    self.assertEqual(reverse_str('dog'), 'god');
  
  def test_is_palindrome(self):
    self.assertTrue(is_palindrome('racecar'));
    self.assertFalse(is_palindrome('racing'));
    # Case sensitivity:
    self.assertTrue(is_palindrome('Racecar'));
  def test_factorial(self):
    self.assertEqual(factorial(5), 120);
    self.assertEqual(factorial(3), 6);
    # handles value errors:
    # NOTE We could pass a bad value directly to our code:
    
    # self.assertRaises(ValueError, factorial(-5))
    
    # NOTE this will break our code. Instead we should pass assertRaises 3 args:
    self.assertRaises(ValueError, factorial, -5);
    # now assertRaises tries to break our funcs, but does not actually execute broken code;