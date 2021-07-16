#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3812/
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        if nums[1] < nums[0]:
            return 0
        if nums[n-2] < nums[n-1]:
            return n-1 
        def PeakElementUtils(start ,end ,nums):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] < nums[mid-1]:
                    end = mid
                else:
                    start = mid+1
            return -1
        return PeakElementUtils(1,n-2,nums)

        
print(Solution().findPeakElement([1, 2, 3, 1]))
