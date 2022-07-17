# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8

"""
Iterative approach.
We hardcode 0 and 1 as initial elements
Big O -> O(n)
"""
def fibonacciIterative(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    a, b = 0, 1
    answer = a + b
    for f in range(3,n+1):
      a = b
      b = answer
      answer = a + b

  return answer

"""
Another Iterative approach using array
Big O -> O(n)
"""
def fibonacciIterative2(n):
  arr = [0,1]
  for i in range(2,n+1):
    arr.append(arr[i-2] + arr[i-1])
  return arr[n]

  
"""
Solving Fibonacci series recursively seems quite simple,
but you need to understand it properly.
Refer: https://realpython.com/fibonacci-sequence-python/
(check section "Examining the Recursion Behind the Fibonacci Sequence")
Big 0 -> (2^n) (called as exponential, horrible time complexity)
"""
def fibonacciRecursive(n):
  if n < 2:
    return n

  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

print(fibonacciIterative(6))
print(fibonacciIterative2(6))
print(fibonacciRecursive(6))
