"""
Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop
"""

def findFactorialRecursive(number):
  """
  This is the base case.
  We always want to return 1 for anything < 2 since 1! and 0! is always 1
  """
  if number < 2:
    return 1
  """
  This is the recursive case.
  We keep recursing till we hit the base case and return from there.
  Then each recursive function will keep returning based on the below
  return statement.
  """
  return number * findFactorialRecursive(number-1)



def findFactorialIterative(number):
  """
  Same as above - we always want to return 1 for anything < 2 since 1! and 0! is always 1, hence we start with val = 1 and the loop starts from 2.
  """
  val = 1
  for _ in range(2,number+1):
    val = val * _
  return val
  
print(findFactorialRecursive(2))
print(findFactorialIterative(2))