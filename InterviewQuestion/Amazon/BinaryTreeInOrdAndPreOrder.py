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
        inOrderHash = dict()
        n = len(preorder)
        m = len(inorder)
        for i in range(m):
            inOrderHash[inorder[i]] = i

        def buildTreeHelper(preStart, inStart, inEnd, preEnd):
            if preStart>=preEnd or inStart >=inEnd:
                 return None
            root = TreeNode(preorder[preStart])
            InOIndex = inOrderHash[root.val]
            root.left = buildTreeHelper(preStart+1, inStart, InOIndex, preEnd)
            root.right = buildTreeHelper(preStart+InOIndex-inStart+1, InOIndex+1, inEnd, preEnd)
            return root
        return buildTreeHelper(0,0,m,n)


if __name__ == "__main__":
    ObjS = Solution()
    print(ObjS.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).val)
