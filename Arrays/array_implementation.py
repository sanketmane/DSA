# Array implementation

class MyArray:
  def __init__(self):
    self.length = 0
    self.data = {}

  def get(self,index):
    return self.data[index]

  def push(self,item):
    self.data[self.length] = item
    self.length += 1
    return self.data

  def pop(self):
    del self.data[self.length - 1]
    self.length -= 1
    return self.data

  

  def delete(self,index):
    for i in range(index,self.length-1):
      self.data[i] = self.data[i+1]

    del self.data[self.length-1]
    self.length -= 1
    return self.data

  

arr = MyArray()
arr.push('hi')
arr.push('are')
arr.push('you')
arr.push('there')
arr.delete(1)
print(arr.data)

