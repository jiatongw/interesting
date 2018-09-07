class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Print tree in level order
def levelOrder(root):
    if not root:
        return []

    res = []
    q = []
    q.append(root)

    while len(q) != 0:
        level = []
        size = len(q)
# level order traverse
        for i in range(0, size):
            root = q.pop(0)
            level.append(root.val)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
        res.append(level)
    return res

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
# Expected level order would be: [[1], [2, 3], [4, 5]]
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    print("The level order of this binary tree is:", levelOrder(node1))