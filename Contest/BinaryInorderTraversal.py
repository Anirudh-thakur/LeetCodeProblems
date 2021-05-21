#https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def __init__(self):
        self.InorderList = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Append data to list 
        self.InorderAppend(root)
        #Return List 
        return self.InorderList

    def InorderAppend(self,root):
        if root != None:
            self.InorderAppend(root.left)
            self.InorderList.append(root.val)
            self.InorderAppend(root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    objS = Solution()
    result = objS.inorderTraversal(root)
    print(result)
        
