# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        _len = len(nums)
        mid = _len // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


if __name__ == '__main__':
    s=Solution()
    nums=[-10,0,1,2,3]
    m = s.sortedArrayToBST(nums)
    
    print(m.val)