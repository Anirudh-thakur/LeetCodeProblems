class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        result = -1
        for i in range(len(n)):
            check = int(n[i])
            if check > result:
                result = check
            if result == 9:
                break
        return result
if __name__ == "__main__":
    ObjS = Solution()
    print(ObjS.minPartitions("27346209830709182346"))
