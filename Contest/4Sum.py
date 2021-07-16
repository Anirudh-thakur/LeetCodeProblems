#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3816/
from collections import defaultdict
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Sum_dict = defaultdict(lambda : None)
        n = len(nums)
        if n < 4:
            return 
        for i in range(n):
            for j in range(i+1,n):
                sum = nums[i] + nums[j]
                if Sum_dict[sum] == None:
                    Sum_dict[sum] = [[i,j]]
                else:
                    temp = Sum_dict[sum]
                    temp.append([i,j])
                    Sum_dict[sum] = temp
        result = []
                    
        for sum in  Sum_dict.keys():
            if Sum_dict[target-sum] != None:
                for l1 in Sum_dict[sum]:
                    for l2 in Sum_dict[target-sum]:
                        temp = [l1[0] , l1[1] , l2[0] , l2[1]]
                        if len(set(temp)) == len(temp):
                            ans = [nums[l1[0]], nums[l1[1]], nums[l2[0]], nums[l2[1]]]
                            ans.sort()
                            if ans not in result:
                                result.append(ans)
        return result


print(Solution().fourSum([2, 2, 2, 2, 2], target=8))
