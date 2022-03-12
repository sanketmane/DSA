# Queue implementation using Linked List
# Queues are FIFO(first in first out)
# Since we are doing this based on LinkedList, we will use "first" and "last" as identifiers in queue
# In our case, Google will get added and removed first
# In linear terms, queue will look like below:
# (first)              (last)
# Google -> Amazon -> Microsoft

# create node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Queue class
class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0
    
  # check whats at the first end of the queue
  def peek(self):
    if self.length > 0:
      return self.first.data
    return "Empty Queue!"

  # push to the queue or enqueue
  def enqueue(self, data):
    node = Node(data)

    if self.length == 0:
      self.first = node
      self.last = self.first
      self.length += 1
    else:
      self.last.next = node
      self.last = node
      self.length += 1

  # remove first item from queue/dequeue
  def dequeue(self):
    if self.length == 0:
      print('Empty Queue, cannot dequeue further!')
      return
      
    self.first = self.first.next
    self.length -= 1

  # check if queue is empty
  def is_empty(self):
    if self.length == 0:
      return True

myQueue = Queue()

myQueue.enqueue('Google')
myQueue.enqueue('Amazon')
myQueue.enqueue('Microsoft')

myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()

print(myQueue.length)
print(myQueue.peek())
print(myQueue.is_empty())