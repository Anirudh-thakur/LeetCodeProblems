#https: // leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3738/
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        if n <= 2:
            return 0
        dyn = [0 for i in range(n)]
        i = 2
        while(i<n):
#            print("number:"+str(i))
            if dyn[i] == 0:
                result = result + 1
                dyn[i] = 1
                p = i * i
                while(p<n):
#                    print("Square number:"+str(p))
                    dyn[p] = -1
                    p = p + i
            i = i+1
#        print(dyn)
        return result
if __name__ == '__main__':
    obj = Solution()
    result = obj.countPrimes(1000)
    print(result)
