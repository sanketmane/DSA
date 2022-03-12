# Interview question
# Implement queue using 2 stacks.
# Since python doesn't have an underlying datastructure of stacks, we can use arrays/lists here.
# The reason for using 2 arrays can be seen in the push method below
# This is nicely explained here: https://www.youtube.com/watch?v=nPvjcQBplH4

class MyQueue:
  def __init__(self):
    # initialize the 2 stacks
    self.stack1 = []
    self.stack2 = []

  # In the push method, we will use stack2 to move things from stack1 to it since     # we want to implement queue but stacks are LIFO. We then push the new
  # element in the stack1 and then move back the elements from stack2 to stack1.
  # So every element that we push in stack1, we are doing O(n) operation
  def push(self,data):
    if len(self.stack1) == 0:
      return self.stack1.append(data)
    
    while self.stack1:
      self.stack2.append(self.stack1.pop())

    self.stack1.append(data)

    while self.stack2:
      self.stack1.append(self.stack2.pop())

  # pop method is straightforward, just pop last item from that stack1
  def pop(self):
    return self.stack1.pop()

  # similar to pop(), return last item from stack1
  def peek(self):
    return self.stack1[-1]

  # return True if the len(stack1) is zero
  def is_empty(self):
    return len(self.stack1) == 0


myqueue = MyQueue()

myqueue.push('Google')
myqueue.push('Amazon')
myqueue.push('Microsoft')

# print(myqueue.stack1)

print(myqueue.peek())
myqueue.pop()
print(myqueue.peek())
myqueue.pop()

print(myqueue.is_empty())