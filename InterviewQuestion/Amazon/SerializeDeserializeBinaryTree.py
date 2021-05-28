#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serializeHelper(root):
            if root == None:
                return '*'
            left = serializeHelper(root.left)+","
            right = serializeHelper(root.right)
            return str(root.val)+"," + left+right
            
        result = serializeHelper(root)
        return result

    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        Queue = data.split(",")
        def deserializeHelper(queue):
            val = queue.pop(0)
            if val == '*':
                return None
            root = TreeNode((val))
            root.left = deserializeHelper(queue)
            root.right = deserializeHelper(queue)
            return root
        return deserializeHelper(Queue)


root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(4)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(ans.val)
print(ans.right.val)
print(ans.left.val)
