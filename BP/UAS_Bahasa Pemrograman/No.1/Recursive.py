class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
def count_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(count_leaf_nodes(root))