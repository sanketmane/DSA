# Hash Table implementation

class HashTable:
  def __init__(self,size):
    self.size = size
    self.data = [None] * self.size # put some gibberish to reserve memory space of the list/array.

  # andreas hash function
  def _hash(self,key):
    hash = 0
    key = key
    for i in range(len(key)):
      hash = (hash + ord(key[i]) * i) % self.size
    return hash


  def set(self,key,val):
    index = self._hash(key) # the above hash function returns an index value
    if self.data[index] == None:
      self.data[index] = [] # create an array to solve the problem of hash collisions
    self.data[index].append([key, val]) # push new array of key,val pairs to the (above) just created array.
    return self.data


  def get(self,key):
    index = self._hash(key)
    if self.data[index]: # check if something exists at that index
      for x in self.data[index]: # loop over the 2d array and match on the key to get the value
        if x[0] == key:
          return x[1]
    return None


myHashTable = HashTable(50)

myHashTable.set('grapes', 10000)
print(myHashTable.data)
print(myHashTable.get('grapes'))

myHashTable.set('apples', 54)
print(myHashTable.data)
print(myHashTable.get('apples'))

myHashTable.set('oranges', 12)
print(myHashTable.data)
print(myHashTable.get('oranges'))