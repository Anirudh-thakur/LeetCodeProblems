class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1:
            return 0
        i = 0
        j = 1
        result = 0
        while j < n:
#            print(prices)
#            print("result:"+str(result))
#            print(i)
#            print(j)
            if prices[j-1] > prices[j]:
                result = result + (prices[j-1] - prices[i])
                i = j
            j+=1
        if j != i:
            result = result + (prices[j-1] - prices[i])
        return result



if __name__ == '__main__':
    ObjS = Solution()
    result = ObjS.maxProfit([7, 1, 5, 3, 6, 4])
    print(result)
