#https://leetcode.com/problems/ugly-number-ii/

from heapq import heapify, heappop
import heapq


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 0
        q = 0
        r = 0
        result = [1]
        ansSet = {1}
        i = 1
        while(i<n):
            k1 = result[p] * 2
            k2 = result[q] * 3
            k3 = result[r] * 5
            k = min(k1,k2,k3)
            if k == k1:
                p+=1
            elif k == k2:
                q+=1
            else:
                r+=1
            if k not in ansSet:
                ansSet.add(k)
                result.append(k)
                i+=1
        return result[n-1]
         


    
    
if __name__ == '__main__':
    objS = Solution()
    result = objS.nthUglyNumber(129)
    print(result)
