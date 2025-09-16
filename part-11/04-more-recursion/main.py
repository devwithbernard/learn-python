# Binary tree

class Node:
    def __init__(self, value, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        print(self.value)

        if self.right:
            self.right.inorder_traversal()

    def pre_traversal(self) -> None:
        print(self.value)

        if self.left:
            self.left.inorder_traversal()

        if self.right:
            self.right.inorder_traversal()

    def find(self, value) -> bool:
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True

    def greatest_node(self):
        if self.right is None:
            return self.value
        else:
            return self.right.greatest_node()


tree = Node(10)
tree.insert(3)
tree.insert(4)
tree.insert(11)
tree.insert(23)
tree.insert(1)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(17)
tree.insert(24)
tree.insert(6)

print(tree.find(18))
print(tree.find(7))
print(tree.find(6))

print(tree.greatest_node())