# Doubly LinkedList is same as Singly LinkedList just that the next node also has pointer to previous node.

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  def append(self,data):
    node = Node(data)

    if self.head == None:
      self.head = node
      self.tail = self.head
      self.length += 1
    else:
      self.tail.next = node
      self.tail = node
      node.prev = self.head
      self.length += 1


  def prepend(self,data):
    node = Node(data)

    node.next = self.head
    self.head.prev = node
    self.head = node
    self.length += 1


  def traverse_to_index(self,index):
    counter = 0
    current_node = self.head
    while counter != index:
      current_node = current_node.next
      counter += 1
    return current_node



  def insert(self,index,data):
    if index == 0:
      return self.prepend(data)
    
    if index >= self.length:
      return self.append(data)

    node = Node(data)

    leader = self.traverse_to_index(index - 1)
    holding_pointer = leader.next
    leader.next = node
    node.next = holding_pointer
    node.prev = leader
    self.length += 1


  def remove(self,index):
    if index == 0:
      next_node = self.head.next
      self.head = next_node
      self.head.prev = None
      self.length -= 1
      return

    if index >= self.length:
      print("index is greater then current length of linkedlist")
      return
    
    current_node = self.traverse_to_index(index)
    leader = self.traverse_to_index(index - 1)
    if self.tail == current_node:
      leader.next = None
      self.tail = leader
    else:
      holding_pointer = self.traverse_to_index(index).next
      leader.next = holding_pointer
      holding_pointer.prev = leader
    self.length -= 1

  def print_list(self):
    myarray = []
    current_node = self.head
    while current_node != None:
      myarray.append(current_node.data)
      current_node = current_node.next
    print(myarray)
    

myLinkedList = DoublyLinkedList()
myLinkedList.append(10)
print(myLinkedList.head.data, myLinkedList.head.next, myLinkedList.head.prev)
print(myLinkedList.tail.data, myLinkedList.tail.next,myLinkedList.tail.prev)
print(myLinkedList.length)

myLinkedList.append(33)
print(myLinkedList.head.data, myLinkedList.head.next, myLinkedList.head.prev)
print(myLinkedList.tail.data, myLinkedList.tail.next,myLinkedList.tail.prev)
print(myLinkedList.length)

myLinkedList.prepend(71)
print(myLinkedList.head.data, myLinkedList.head.next, myLinkedList.head.prev)
print(myLinkedList.tail.data, myLinkedList.tail.next,myLinkedList.tail.prev)
print(myLinkedList.length)

myLinkedList.insert(1,95)
print(myLinkedList.head.data, myLinkedList.head.next, myLinkedList.head.prev)
print(myLinkedList.tail.data, myLinkedList.tail.next,myLinkedList.tail.prev)
print(myLinkedList.length)

myLinkedList.remove(3)
print(myLinkedList.head.data, myLinkedList.head.next, myLinkedList.head.prev)
print(myLinkedList.tail.data, myLinkedList.tail.next,myLinkedList.tail.prev)
print(myLinkedList.length)

myLinkedList.print_list()

#[71,95,10,33]