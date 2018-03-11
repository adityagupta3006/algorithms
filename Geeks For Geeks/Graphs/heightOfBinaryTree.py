class Node(object):
    """docstring for node"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def calcHeight(node):
    if node is None:
        return
    height = 0
    q = []
    q.append(node)
    
    while True:
        l = len(q)
        if l == 0:
            return height

        height += 1

        while l > 0:
            current = q.pop()
            if current.left:
                q.append(current.left)
            
            if current.right:
                q.append(current.right)

            l -= 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#root.right.left = Node(6)
#root.right.right = Node(7)
print calcHeight(root)