#https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
import itertools
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 1:
            root = TreeNode(1)
            return [root]
        if n == 2:
            root1 = TreeNode(1)
            root1.right = TreeNode(2)
            root2 = TreeNode(2)
            root2.left = TreeNode(1)
            return [root1, root2]
        nList = []
        for i in range(1, n+1):
            nList.append(i)
        permutation_list = list(itertools.permutations(nList))
        print(permutation_list)
 #       print(nList)
        print(len(permutation_list))
        result = []
        for perms in permutation_list:
            root = TreeNode(perms[0])
            result.append(root)
            for i in range(1, len(perms)):
                self.AddBST(root, perms[i])
        checkResult = list(result)
        for i in range(0, len(checkResult)):
            for j in range(i+1, len(checkResult)):
 #               print(checkResult[i].val)
 #               print(checkResult[j].val)
                check = self.sameTree(checkResult[i], checkResult[j])
 #               print(check)
                if check:
                    if checkResult[j] in result:
                     result.remove(checkResult[j])
        return result

    def sameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        result = p.val == q.val
        if result == False:
            return False
        result = result and self.sameTree(p.left, q.left)
        result = result and self.sameTree(p.right, q.right)
        return result

    def AddBST(self, root, data):
        if root != None:
            if root.val > data:
                if root.left == None:
                    root.left = TreeNode(data)
                else:
                    self.AddBST(root.left, data)
            else:
                if root.right == None:
                    root.right = TreeNode(data)
                else:
                    self.AddBST(root.right, data)
        else:
            root = TreeNode(data)
      

if __name__ == '__main__':
    objS = Solution()
    result = objS.generateTrees(7)
    print(len(result))
    print()
    for root in result:
        print(root.val,end=" ")
