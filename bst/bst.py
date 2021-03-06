# Tree traversal in Python


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + ",", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + ",", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + ",", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(58)
root.left = Node(35)
root.right = Node(90)
root.left.left = Node(30)
root.left.right = Node(43)
root.left.left.left = Node(25)
root.left.left.right = Node(34)
root.left.right.left = Node(42)
root.right.right = Node(98)
root.right.left = Node(78)
root.right.left.left = Node(75)
root.right.left.left.right= Node(76)
root.right.left.right= Node(85)
root.right.right.right= Node(100)
root.right.right.left= Node(92)
root.right.right.left.right= Node(93)


print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)