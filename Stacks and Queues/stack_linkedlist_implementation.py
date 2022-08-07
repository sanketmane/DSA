# Stack implementation using Linked Lists.
# Like we had head and tail part in Linked Lists, we will use a similar approach in stacks as well. Here we will use "top" and "bottom" to indicate what is at the top and bottom of the stack respectively.

# Create a node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    # Initialize your stack with basic attributes like LinkedList
    self.top = None
    self.bottom = None
    self.length = 0

  # check whats at the top of the stack
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

  # push at the end of the stack
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
      """
      Note that we are not changing bottom part in the else loop since it is alrady taken
      care when there is not element in the stack i.e the 'if' part of the loop.
      """
      
  # pop from the end of the stack  
  def pop(self):
    if self.length == 0:
      print("Stack is empty, cannot pop further!")
      return
      
    self.top = self.top.next
    self.length -= 1

  # check if stack is empty
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

