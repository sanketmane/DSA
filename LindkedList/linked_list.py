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
      
      # if index = 0 then prepend
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
      
      
      current_node = self.traverse_to_index(index) # capture the current node
      leader = self.traverse_to_index(index - 1) # capture the leader node
      
      # if current node and tail node is same then move tail to leader
      if self.tail == current_node:
        leader.next = None # as leader is tail node, the next pointer = None
        self.tail = leader # set leader node as tail node
      
      # otherwise point the leader node to node next to removal node
      else:
        holding_pointer = current_node.next
        leader.next = holding_pointer
        holding_pointer.prev = leader
      self.length -= 1


    # Reversing a linked list(interview question)
    # A ------> B --------> C ----------> D -> None
    #(first)  (second)     (third)
    # we will basically move the first and second pointer till second is null

    # A <- B <- C <- D <- None (Reverse)

    def reverse(self):
      if self.length == 0: # if there is only element in ll, then just return it.
        return self.head

      first = self.head # grab head element
      second = self.head.next # grab the second element
      self.tail = self.head # tail becomes head in reverse direction

      while second: # idea is to loop till the second element is null(this "-->" direction)
        temp = second.next # grab the third element
        second.next = first # set the pointer for second to first
        first = second # make the current second as first(rememember we are moving left)
        second = temp # make the current third as second(same as above)

      self.head.next = None # make head point to null
      self.head = first # after the above while loop finishes, earlier last element becomes first, so make it head

      return self.print_list() # finally print the reverse array using the print list method

   

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
# print(myLinkedList.head.data, myLinkedList.head.next)
# print(myLinkedList.tail.data, myLinkedList.tail.next)
# print(myLinkedList.length)

myLinkedList.append(20)
# print(myLinkedList.head.data, myLinkedList.head.next)
# print(myLinkedList.tail.data, myLinkedList.tail.next)
# print(myLinkedList.length)

myLinkedList.prepend(55)
# print(myLinkedList.head.data, myLinkedList.head.next)
# print(myLinkedList.tail.data, myLinkedList.tail.next)
# print(myLinkedList.length)

myLinkedList.insert(3,66)
# print(myLinkedList.head.data, myLinkedList.head.next)
# print(myLinkedList.tail.data, myLinkedList.tail.next)
# print(myLinkedList.length)

# myLinkedList.remove(3)
# print(myLinkedList.head.data, myLinkedList.head.next)
# print(myLinkedList.tail.data, myLinkedList.tail.next)
# print(myLinkedList.length)

myLinkedList.print_list()

myLinkedList.reverse()