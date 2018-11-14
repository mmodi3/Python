from queue import Queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def levelOrder(root):
    #type root: TreeNode
    res = []
    q = Queue()
    q.put(root)
    while q.qsize():
        tempnode = q.get()
        if tempnode.left:
            q.put(tempnode.left)
        if tempnode.right:
            q.put(tempnode.right)
        res.append(tempnode.val)
    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)
print(levelOrder(root))
