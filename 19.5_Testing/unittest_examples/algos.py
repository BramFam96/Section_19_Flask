def reverse_str(str):
  '''Returns str input reversed'''
  return str[::-1]

def is_palindrome(s):
  '''Checks if input string is a palindrome'''
  rev = reverse_str(s)
  return s.lower() == rev.lower();

def factorial(n):
  '''Calculates factorials'''
  if type(n) != int or n <= 0:
    raise ValueError("'n' must be non-negative integer")
  result =1
  for i in range(2, n+1):
    result *= i
  return result;
  # NOTE from here we create a seperate test file:
  # check test_algos.py
  # We then run these with:
  # python -m unittest test_algos.py -> HOWEVER
  # NOTE Using common naming patterns like test_[module] 
  # allows us vscode to automatically run our tests;
  
  # In VSCode -> Open preferences: Ctrl+Shift+P -> type 'tests' 
  # Select Python: Run All Tests
