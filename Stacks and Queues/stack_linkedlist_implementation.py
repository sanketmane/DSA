# Stack implementation using Linked Lists.

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    if self.length > 0:
      return self.top.data
    else:
      return "Stack is empty!"
    
      
# Stack should push in the following order: 
# Apple (top)
# Microsoft
# Amazon
# Google (bottom)
  
  def push(self,data):
    node = Node(data)

    if self.length == 0:
      self.top = node
      self.bottom = self.top
      self.length += 1
    else:
      node.next = self.top
      self.top = node
      self.length += 1
      
    
  def pop(self):
    if self.length == 0:
      print("Stack is empty, cannot pop further!")
      return
      
    self.top = self.top.next
    self.length -= 1


  def is_empty(self):
    if self.length == 0:
      return True
      
myStack = Stack()

myStack.push('Google')
myStack.push('Amazon')
myStack.push('Microsoft')
myStack.push('Apple')

myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
print(myStack.peek())

