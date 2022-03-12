# Stack implementation using arrays/list
# Probably pretty simple compared to Linked List.

class Stack:
  def __init__(self):
    self.arr = [] # initialize your array

  # check whats at the top of the stack
  def peek(self):
    if len(self.arr) > 0:
      return self.arr[-1]
    else:
      return "Stack is empty!"

  # push at the end of the stack
  def push(self,data):
    return self.arr.append(data)

  # pop from end of the stack
  def pop(self):
    if len(self.arr) == 0:
      print("Stack is empty, cannot pop further!")
      return
    
    return self.arr.pop()

  # check if stack is empty  
  def is_empty(self):
    if len(self.arr) == 0:
      return True


myStack = Stack()

myStack.push('Google')
myStack.push('Amazon')
myStack.push('Microsoft')

myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
print(myStack.peek())
print(myStack.is_empty())
print(myStack.arr)
