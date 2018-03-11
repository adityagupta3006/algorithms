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
    
    while (q):
        height = len(q)
        current = q.pop()
        
        if current.left:
            q.append(current.left)        

        if current.right:
            q.append(current.right)




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
calcHeight(root)


'''
def treeHeight(node):
    if node is None:
        return

        q = []
        q.append(node)
        h = 0

        while(True):
            nodeCOunt = len(q)
            if nodeCOunt == 0:
                return height

            height += 1

            while (nodeCOunt > 0):
                node = q[0]
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                nodeCount -= 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "Height of tree is", treeHeight(root)

'''