__author__ = 'liusong'

# Link: https://github.com/qiwsir/algorithm/blob/master/binary_tree.md

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    # Compose a Binary Sort Tree
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    # Search a node.
    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    # Print the Binary Sort Tree.
    def print_bst(self):
        if self.left:
            self.left.print_bst()
        print self.data
        if self.right:
            self.right.print_bst()

    # Count the children node.
    def children_count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    # Delete a Node.
    def delete_node(self, data):
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # Delete this node if it has no children node.
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                # Use the children node to replace the node if it has only one children node.
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                # Need to check all the children node if it has two children node.
                # Don't understand this section. ??
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.date = successor.data
                if parent.left == successor:
                    parent.left = successor.left
                else:
                    parent.right = successor.right


# Compose a Binary Sort Tree.
root = Node(8)
root.insert(1)
root.insert(10)
root.insert(4)
root.insert(6)
root.insert(14)
root.insert(13)
root.insert(7)
root.insert(3)

# Lookup a node.
print root.lookup(6)[0], root.lookup(6)[1]
print root.lookup(9)[0], root.lookup(9)[1]

# Print a binary sort tree.
root.print_bst()

# Delete a node.
root.delete_node(3)
root.print_bst()
