#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3739/
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(cardPoints)-1
        if k == 1:
            return max(cardPoints[0],cardPoints[end])
        if k == end+1:
            return sum(cardPoints)
        prevSum = []
        prevSum.append(cardPoints[0])
        for i in range(1,k):
            prevSum.append(prevSum[i-1] + cardPoints[i])
        nextSum = []
        nextSum.append(cardPoints[end])
        for i in range(1,k):
            nextSum.append(nextSum[i-1] + cardPoints[end-i])
        print(prevSum)
        print(nextSum)
        result = max(prevSum[k-1],nextSum[k-1])
        for i in range(0,k-1):
            check = prevSum[i]+nextSum[k-i-2]
            if check > result:
                result = check
        return result
       # result = self.GetMax(cardPoints,k,start,end)
       # return result

    def GetMax(self, cardPoints, k, start, end):
        if k == 0:
            return 0
        if k == 1:
            return max(cardPoints[start],cardPoints[end])
        if start>=end:
            return 0
        return max(cardPoints[start]+self.GetMax(cardPoints, k-1, start+1, end), cardPoints[end]+self.GetMax(cardPoints, k-1, start, end-1))

if __name__ == '__main__':
    cardPoints = [30,88,33,37,18,77,54,73,31,88,93,25,18,31,71,8,97,20,98,16,65,40,18,25,13,51,59] 
    k = 26
    obj = Solution()
    result = obj.maxScore(cardPoints, k)
    print(result)
