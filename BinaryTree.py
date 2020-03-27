
# From what I understood from the example the structure that I have to create
# is a binary tree without any specific set of rules, like BST.


# The tree will consist of objects with value and two pointers to two other objects from the same class

import time


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

# To get a sum of all the values below given node - start, I just used an algorithm that adds its value
# to the sum and repeats itself for both of the child nodes as long as they exist

    def get_sum(self, start):
        node_value = 0
        if start:
            node_value += start.value
            node_value += self.get_sum(start.left)
            node_value += self.get_sum(start.right)
        return node_value

# My first idea for getting a number of nodes in a tree was to use class variable that would +=1
# every time new node is created. It be faster than traversing through the tree to count them, but
# I wasn't sure if there will be only one existing three at any time.

    def count_nodes(self, start):
        if start is None:
            return 0
        return 1 + self.count_nodes(start.left) + self.count_nodes(start.right)

    def get_average(self, start):
        return self.get_sum(start)/self.count_nodes(start)

    def get_tab(self, start):

        tab = []
        if start:
            tab.append(start.value)
            tab = tab + self.get_tab(start.left)
            tab = tab + self.get_tab(start.right)
        return tab

    def get_median(self, start):

        tab = self.get_tab(start)
        n = self.count_nodes(start)

        sorted(tab)

        if n % 2 != 0:
            return float(tab[n / 2])

        return float((tab[int((n - 1) / 2)] + tab[int(n / 2)]) / 2.0)


def test_tree(node):
    print(node.get_sum(node.root))
    print(node.count_nodes(node.root))
    print(node.get_average(node.root))
    print(node.get_median(node.root))


def test_time(fun, start, n ):

    t0 = time.time()
    for i in  range(n):
        fun(start)
    t1 = time.time()
    return t1-t0


# recreation of the tree from the example:

tree = BinaryTree(5)
tree.root.left = Node(3)
tree.root.right = Node(7)
tree.root.left.left = Node(2)
tree.root.left.right = Node(5)
tree.root.right.left = Node(1)
tree.root.right.right = Node(0)
tree.root.right.right.left = Node(2)
tree.root.right.right.right = Node(8)
tree.root.right.right.right.right = Node(5)


test_tree(tree)
print(test_time(tree.get_sum, tree.root, 1000))
