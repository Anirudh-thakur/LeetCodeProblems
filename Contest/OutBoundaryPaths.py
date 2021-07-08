#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3790/
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        for _ in range(maxMove):
            dp = [[((i==0 or dp[i-1][j]) + (i == m-1 or dp[i+1][j]) + (j == 0 or dp[i][j-1]) 
            + (j == n-1 or dp[i][j+1])) for j in range(n)] for i in range(m) ]
            print(dp)
        return dp[startRow][startColumn] % (10 ** 9 + 7)


print(Solution().findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
