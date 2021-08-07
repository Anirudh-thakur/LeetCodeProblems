#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3831/
import sys
from collections import defaultdict
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        ZeroDict = []
        OneDict = []

        result = [[0 for _ in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ZeroDict.append([i,j])
                else:
                    OneDict.append([i,j])
        for Ones in OneDict:
            i = Ones[0]
            j = Ones[1]
            minDist = sys.maxsize
            for Zero in ZeroDict:
                k = Zero[0]
                l = Zero[1]
                minDist = min(minDist,abs(i-k)+abs(j-l))
                if minDist == 1:
                    break
            result[i][j] = minDist
        return result


        
print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))