# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.left == None:
            return False
        if root.left.val != root.right.val:
            return False
        return self.findSymmetry(root.left,root.right)
    def findSymmetry(self,p,q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        result = self.findSymmetry(p.left,q.right)
        result = result and self.findSymmetry(p.right,q.left)
        return p.val == q.val and result


if __name__ == '__main__':
    objS = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    result = objS.isSymmetric(root)
    print(result)