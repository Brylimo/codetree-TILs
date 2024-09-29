class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n = int(input())

tree = [None] * n

for i in range(n):
    tree[i] = Node(chr(ord('A') + i))

for _ in range(n):
    me, left, right = input().split()
    me = ord(me) - ord('A')

    left_node, right_node = None, None
    if left != '.':
        left_node = tree[ord(left) - ord('A')]
    if right != '.':
        right_node = tree[ord(right) - ord('A')]

    tree[me].left = left_node
    tree[me].right = right_node

def preorder(x):
    if x is None:
        return

    print(x.data, end="")
    preorder(x.left)
    preorder(x.right)

def inorder(x):
    if x is None:
        return

    inorder(x.left)
    print(x.data, end="")
    inorder(x.right)

def postorder(x):
    if x is None:
        return

    postorder(x.left)
    postorder(x.right)
    print(x.data, end="")

preorder(tree[0])
print()
inorder(tree[0])
print()
postorder(tree[0])
print()