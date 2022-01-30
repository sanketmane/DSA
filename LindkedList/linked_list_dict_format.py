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

class LinkedList:
    def __init__(self, value):
        # create head node
        self.head = {'value': value, 'next': None}
        self.tail = self.head  # store current head value and also acts as pointer
        self.length = 1

    def append(self, value):
        # create new node to be used as last node
        newNode = {'value': value, 'next': None}
        self.tail['next'] = newNode  # tail next should point to new value
        self.tail = newNode  # move the tail to this new node
        self.length += 1
        return self.head  # as we see constructor head is still pointing to original memory location

    def prepend(self, value):
        newNode = {'value': value, 'next': None}
        newNode['next'] = self.head  # new node points to head
        self.head = newNode  # replace head with new node
        self.length += 1
        return self.head

    # method to traverse till the index of a given node
    def traverseToIndex(self,index):
      counter = 0
      currentNode = self.head
      while counter != index:
        currentNode = currentNode['next']
        counter += 1
      return currentNode

    
    def insert(self,index,value):
      # if index provided is greater than length
      # of the LinkedList then append to the end of LL.
      if index >= self.length:
        return self.append(value)

      # index = 0 will break the traverseToIndex method
      if index == 0:
        return self.prepend(value)
  
      # create new node just like for append and prepend methods
      # created above.
      newNode = {
        'value': value,
        'next' : None
      }

      # *(leader)  (some node that leader is pointing to)
      #         \ /
      #          *(insert node)
      
      # capture the leader node, note leader index - 1
      leader = self.traverseToIndex(index - 1)
      holdingPointer = leader['next'] # pointer to hold existing state
      leader['next'] = newNode # pointer the leader to newNode
      newNode['next'] = holdingPointer # point newNode to node that leader was pointing to earlier
      self.length += 1
      return self.head


    def remove(self,index):
      # if index = 0, traverseToIndex method will fail.
      if index == 0:
        holdingPosition = self.head['next'] # grab the pointer of current head
        self.head = holdingPosition # move head to the above pointer
        self.length -= 1
        return self.head

      #grab the leader node
      leader = self.traverseToIndex(index - 1)
      # grab the current pointer of node to be deleted
      holdingPosition = self.traverseToIndex(index)['next']
      # point leader to the current position of node to be deleted
      leader['next'] = holdingPosition
      self.length -= 1
      return self.head



    # to get list/array of node values
    def printList(self):
        myarray = []
        currentNode = self.head # start with head value
        while currentNode != None:
            myarray.append(currentNode['value'])
            currentNode = currentNode['next']
        return myarray


myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)

myLinkedList.prepend(24)
myLinkedList.insert(3,100)
myLinkedList.insert(0,50)
print(myLinkedList.printList())
print(myLinkedList.length)
print(myLinkedList.remove(0))
print(myLinkedList.length)
print(myLinkedList.printList())

