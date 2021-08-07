#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3829/
class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [i for i in range(1,n+1)]
        def beautifulArrayHelper(result):
            if len(result) <= 1: return result
            return beautifulArrayHelper(result[::2]) + beautifulArrayHelper(result[1::2])
        return beautifulArrayHelper(result)

print(Solution().beautifulArray(5))            
