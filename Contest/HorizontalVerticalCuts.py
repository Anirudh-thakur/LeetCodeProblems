#https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3766/

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        print(horizontalCuts)
        maxH = max(horizontalCuts[i] - horizontalCuts[i-1] for i in range(1,len(horizontalCuts)))
        print(maxH)
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        print(verticalCuts)
        maxW = max(verticalCuts[i] - verticalCuts[i-1]
                   for i in range(1, len(verticalCuts)))
        print(maxW)
        print(maxH * maxW)
        print(((pow(10,9)) + 7))
        return (maxH * maxW) % (pow(10, 9) + 7)


h = 50
w = 15
horizontalCuts = [37, 40, 41, 30, 27, 10, 31]
verticalCuts = [2, 1, 9, 5, 4, 12, 6, 13, 11]
print(Solution().maxArea(h,w,horizontalCuts,verticalCuts))
