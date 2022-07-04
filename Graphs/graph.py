"""
Simple Graph implementation
Adjacent List states the neighbours for the given node in a graph
"""

class Graph:
  def __init__(self):
    self.numberOfNodes = 0
    self.adjacentList = {}


  def add_vertex(self,node):
    """
    we are adding a new node/vertex so it has 0 neighbours,
    hence we assign it an empty list.
    """
    self.adjacentList[node] = []
    self.numberOfNodes += 1

  def add_edge(self,node1,node2):
    """
    undirected graph
    append neighbour values to the 'adjacentList' array for the given node
    conversely do the same for the neighbour node as well.
    """
    self.adjacentList[node1].append(node2)
    self.adjacentList[node2].append(node1)

myGraph = Graph()

myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')

print(myGraph.numberOfNodes)

myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4') 
myGraph.add_edge('4', '2') 
myGraph.add_edge('4', '5') 
myGraph.add_edge('1', '2') 
myGraph.add_edge('1', '0') 
myGraph.add_edge('0', '2') 
myGraph.add_edge('6', '5')

print(myGraph.adjacentList)
