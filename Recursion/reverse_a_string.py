# Implement a function that reverses a string using iteration...and then recursion!

"""
Iterative logic
There are multiple ways to implement iterative logic.
"""
def reverseStringIteratively(mystring):
  reverse_string = "".join([str(i) for i in reversed(mystring)])
  return reverse_string

def reverseStringIteratively2(mystring):
  arr = []
  for i in mystring:
    arr.append(i)
  arr.reverse()
  reverse_string = "".join([ str(x) for x in arr ])
  return reverse_string

def reverseStringIteratively3(mystring):
  arr = []
  for i in mystring:
    arr.append(i)
  reverse_string = "".join([ str(i) for i in arr[::-1] ])
  return reverse_string

  
"""
Explanation on how the recursive logic works
reverseStringRecursively('abc')                       #mystring = abc
=reverseStringRecursively('bc') + 'a'                 #mystring[1:] = bc    s[0] = a
=reverseStringRecursively('c') + 'b' + 'a'            #mystring[1:] = c     s[0] = a
=reverseStringRecursively('') + 'c' + 'b' + 'a'
='cba'
"""
def reverseStringRecursively(mystring):
  if len(mystring) == 0: # you can also use mystring == ""
    return mystring

  return reverseStringRecursively(mystring[1:]) + mystring[0]


print(reverseStringIteratively("yoyo mastery"))
print(reverseStringIteratively2("yoyo mastery"))
print(reverseStringIteratively3("yoyo mastery"))
print(reverseStringRecursively("yoyo mastery"))