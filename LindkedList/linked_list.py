# 10 --> 5 --> 16

# pseudo code:
# we will implement linkedlist as nested dictionaries
# myLinkedList = {
#   head: {
#     value: 10
#     next: {
#       value: 5
#       next: {
#         value: 16
#         next: null
#       }
#     }
#   }
# };


# Below is generic solution for Linked List in Python.
# I've also created one using dictionaries. See the LinkedList directory. 
# Node class to capture node attributes
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def append(self,data):
      node = Node(data)
      if self.head == None: # if the linkedlist is empty
        self.head = node # as the linkedlist is empty, new node becomes the head
        self.tail = self.head # since there is only 1 element, head and tail are same
        self.length += 1
      else:
        self.tail.next = node # set the existing tail pointer towards new node
        self.tail = node # new node becomes the tail
        self.length += 1


    def prepend(self,data):
      node = Node(data)
      node.next = self.head # since this is prepend, set new node pointer to current head
      self.head = node # new node becomes the new head
      self.length += 1


    # this method grabs the node for the given index
    def traverse_to_index(self,index):
      counter = 0
      current_node = self.head
      while counter != index:
        current_node = current_node.next
        counter += 1
      return current_node


    # *(leader)  (some node that leader is currently pointing to)
    #         \ /
    #          *(insert node)
    def insert(self,index,data):
      # if index higher/equal to lenght of linkedlist then append to end of list
      if index >= self.length:
        return self.append(data)
      
      # if index = = then prepend
      if index == 0:
        return self.prepend(data)
      
      node = Node(data)

      leader = self.traverse_to_index(index - 1) # grab the leader
      holding_pointer = leader.next # grab the next node to leader
      leader.next = node # point leader to new node
      node.next = holding_pointer # point new node to node that leader was pointing earlier
      self.length += 1



    def remove(self,index):
      # if index - 0 no need to traverse the list
      if index == 0:
        holding_pointer = self.head.next
        self.head = holding_pointer
        self.length -= 1
        return self 

      if index >= self.length:
        print("index shouldn't exceed length of the linkedlist")
      
      leader = self.traverse_to_index(index - 1) # grab the leader
      holding_pointer = self.traverse_to_index(index).next # grab node next to the node for given index
      leader.next = holding_pointer # point the leader to next node
      self.length -= 1

    # print element data values in a list
    def print_list(self):
      myarray = []
      current_node = self.head
      while current_node != None:
        myarray.append(current_node.data)
        current_node = current_node.next
      print(myarray)




myLinkedList = LinkedList()
myLinkedList.append(10)
print(myLinkedList.head.data, myLinkedList.head.next)
print(myLinkedList.tail.data, myLinkedList.tail.next)
print(myLinkedList.length)

myLinkedList.append(20)
print(myLinkedList.head.data, myLinkedList.head.next)
print(myLinkedList.tail.data, myLinkedList.tail.next)
print(myLinkedList.length)

myLinkedList.prepend(55)
print(myLinkedList.head.data, myLinkedList.head.next)
print(myLinkedList.tail.data, myLinkedList.tail.next)
print(myLinkedList.length)

myLinkedList.insert(3,66)
print(myLinkedList.head.data, myLinkedList.head.next)
print(myLinkedList.tail.data, myLinkedList.tail.next)
print(myLinkedList.length)

myLinkedList.remove(3)
print(myLinkedList.head.data, myLinkedList.head.next)
print(myLinkedList.tail.data, myLinkedList.tail.next)
print(myLinkedList.length)

myLinkedList.print_list()