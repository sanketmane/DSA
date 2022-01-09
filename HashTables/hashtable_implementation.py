# Hash Table implementation

class HashTable:
  def __init__(self,size):
    self.size = size
    self.data = [None] * self.size # put some gibberish to reserve memory space of the list/array.

  # andreas hash function which as per him is O(1)
  def _hash(self,key):
    hash = 0
    key = key
    for i in range(len(key)):
      hash = (hash + ord(key[i]) * i) % self.size
    return hash

  # O(1)
  def set(self,key,val):
    index = self._hash(key) # the above hash function returns an index value
    if self.data[index] == None:
      self.data[index] = [] # create an array to solve the problem of hash collisions
    self.data[index].append([key, val]) # push new array of key,val pairs to the (above) just created array.
    return self.data

  # O(1) mostly except for hash collision case where it is O(n)
  def get(self,key):
    index = self._hash(key)
    if self.data[index]: # check if something exists at that index
      for x in self.data[index]: # loop over the 2d array and match on the key to get the value
        if x[0] == key:
          return x[1]
    return None

  # O(n) as we have to loop over all items in the hash table
  def keys(self): # function to get all keys for a hash table
    keysArray = []
    for x in range(len(self.data)):
      if self.data[x] != None:
        keysArray.append(self.data[x][0][0])
    return keysArray



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


print(myHashTable.keys())