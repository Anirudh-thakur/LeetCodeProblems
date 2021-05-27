#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34538/My-Accepted-Java-Solution


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        m = len(preorder)
        return self.buildTreeHelper(0,0,n,m,inorder,preorder)

    def buildTreeHelper(self,startIn, startPre, n, m, inorder, preorder):
        print("start":startIn)
        print(startPre)
        if startIn >= n or startPre >= m:
            return None
        root = TreeNode(preorder[startPre])
        i = inorder.index(preorder[startPre])
        print(root.val)
        print(i)
        root.left = self.buildTreeHelper(startIn,startPre+1,i-1,m,inorder,preorder)
        root.right = self.buildTreeHelper(
            i+1, startPre+i-startIn+1, i+1, m, inorder, preorder)
        return root

if __name__ == "__main__":
    ObjS = Solution()
    print(ObjS.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).val)
