import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_till_now = 0
        max = -float("inf")
        for i in nums:
            max_till_now  = max_till_now  + i
            if max < max_till_now :
                max = max_till_now 
            if max_till_now < 0:
                max_till_now = 0
        return max


if __name__ == '__main__':
    obj = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = obj.maxSubArray(nums)
    print(result)