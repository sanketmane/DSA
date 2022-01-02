# Reverse a string

# Classic approach
def reverse(string):
  if not isinstance(string,str) or len(string) < 2:
    return string

  arr = []
  totalItems = len(string) - 1
  for x in range(totalItems,-1,-1):
      arr.append(string[x])
  return "".join(arr)

print(reverse('Hi this is Optimus'))

# Another way
def reverse2(string):
  arr = list(string)
  arr.reverse()
  return "".join(arr)

print(reverse2('Hi this is Optimus'))


# Dan Bader's preferred way
def reverse3(string):
  arr = []
  for x in reversed(string):
    arr.append(x)
  return "".join(arr)
print(reverse3('Hi this is Optimus'))


# Fastest and easiest
def reverse4(string):
  return string[::-1]

print(reverse4('Hi this is Optimus'))


