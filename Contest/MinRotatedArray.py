#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
 #       print(end)
        pivot = self.getPivot(start,end,nums)
 #       print(pivot)
        if pivot == -1:
            return nums[0]
        return nums[pivot]
    def getPivot(self,start,end,nums):
        while start <= end:
            mid = int((start+end)/2)
 #           print(nums[mid])
            if mid > start and nums[mid] < nums[mid-1]:
                return mid
            if mid < end and nums[mid+1] < nums[mid]:
                return mid+1
            if nums[start] >= nums[mid]:
                end = mid - 1
            else:
                start = mid +1 
        return -1
if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    print(nums)
    objS = Solution()
    result = objS.findMin(nums)
    print(result)