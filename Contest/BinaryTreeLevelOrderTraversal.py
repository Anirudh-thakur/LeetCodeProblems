#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3749/
# Definition for a binary tree node.c
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):

    def __init__(self):
        self.level_dict = []
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.createLevelDictionary(1,root)
        return self.level_dict
    def createLevelDictionary(self,level,root):
        if root == None:
            return
        if level > len(self.level_dict):
            self.level_dict.append([root.val])
        else:
            add = self.level_dict[level-1]
            add.append(root.val)
            self.level_dict[level-1] = add
        self.createLevelDictionary(level+1,root.left)
        self.createLevelDictionary(level+1,root.right)
      

   
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    ObjS = Solution()
    result = ObjS.levelOrder(root)
    print(result)
