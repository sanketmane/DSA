#Pythonic implementation of Binary Search Tree(BST)

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        # set root node to none initially
        self.root = None

    def insert(self, data):
        node = Node(data)

        # if root node is not set, set it first
        if not self.root:
            self.root = node
        # if root node is set, then start from there
        # hence we assign currentNode as root.
        else:
            currentNode = self.root
            while True:
                # check if data is less than currentNode's data,
                # if yes and if there is nothing on left of currentNode,
                # then point our node to its left, else
                # change the currentNode from root to node on left and continue
                # to loop again till we reach currentNode that has nothing to its left.
                if data < currentNode.data:
                    if not currentNode.left:
                        currentNode.left = node
                        return
                    else:
                        currentNode = currentNode.left
                # do the same thing on right node as left node.
                else:
                    if not currentNode.right:
                        currentNode.right = node
                        return
                    else:
                        currentNode = currentNode.right

    # lookup is similar to insert, but the difference we will run
    # the while loop till the currentNode is present.
    # The while loop will be used to keep checking if the node we want to check
    # is there or not.
    def lookup(self, data):
        node = Node(data)

        # check if node matches root node
        if self.root == node:
            return node
        else:
            # set the currentNode as root and start to traverse from there.
            currentNode = self.root
            # loop as long as currentNode is present.
            while currentNode:
                if data < currentNode.data:
                    currentNode = currentNode.left
                elif data > currentNode.data:
                    currentNode = currentNode.right
                # if node is matched, return the exit the loop
                elif currentNode.data == node.data:
                    return currentNode

    """
    Need to complete remove method
    """
    def remove(self,data):
      node = Node(data)

      if self.root == node:
        self.root = self.root.right

    """
    Tree traversal i.e return all values in a tree.
    (Inorder: Left, Root, Right)
    """
    def traversal(self):
      if self.root != None:
         self.print_tree(self.root)

    def print_tree(self, currentNode):
      if currentNode != None:
        self.print_tree(currentNode.left)
        print(currentNode.data)
        self.print_tree(currentNode.right)


# Tree
#      9
#   4     20
# 1  6  15  170

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

# print(tree.root.data)
# print(tree.root.left.data)
# print(tree.root.right.data)
# print(tree.root.left.right.data)

# print(tree.lookup(1).right)

tree.traversal()