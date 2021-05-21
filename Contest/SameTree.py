#https: // leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        result = p.val == q.val
        if result == False:
            return False      
        result = result and self.isSameTree(p.left,q.left)      
        result = result and self.isSameTree(p.right, q.right)
        
        return result

if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    objS = Solution()
    result = objS.isSameTree(root1,root2)
    print(result)

