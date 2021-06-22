#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3786/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        for i in range(1,numRows):
            add = []
            for j in range(i+1):
                if j == 0 or j==i:
                    add.append(1)
                else:
                    add.append(result[i-1][j-1]+result[i-1][j])
            result.append(add)
        return result

print(Solution().generate(5))
