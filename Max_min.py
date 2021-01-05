def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root

def maxValue(root):
    current = root
    while(current.right):
        current = current.right
    return current.data

def minValue(root):
    current = root
    while(current.left):
        current = current.left
    return current.data

root=None
root = insert(root,2)
root = insert(root,0)
root = insert(root,3)
root = insert(root,48)
root = insert(root,12)
print(maxValue(root))
print(minValue(root))
