#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return nums
        temp = nums[0:n-k]
        for i in range(n-k,n):
            nums[i-n+k] = nums[i]
        for i in range(k,n):
            nums[i] = temp[i-k]
        return nums
        
if __name__ == "__main__":
    objS = Solution()
    result = objS.rotate([-1,-100,3,99],2)
    print(result)
