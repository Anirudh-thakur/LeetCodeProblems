#https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.Max = -sys.maxsize
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxPathSumHelper(root):
            if root == None:
                return 0
            left = max(0,maxPathSumHelper(root.left))
            right = max(0,maxPathSumHelper(root.right))
            self.Max = max(self.Max ,root.val+left+right)
            return max(left,right)+root.val
        maxPathSumHelper(root)
        return self.Max
if __name__ == "__main__":
    root =  TreeNode(-10)
    root.left = TreeNode(15)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    print(Solution().maxPathSum(root))
