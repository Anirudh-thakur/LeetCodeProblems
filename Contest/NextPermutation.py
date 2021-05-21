class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = n-1
        while p1 >=0 and nums[p1] <= nums[p1-1]:
            p1 = p1 - 1
        p1 = p1 - 1
        print(p1)
        if p1 >= 0:
            p2 = n-1
            while p2 >=0 and nums[p1] >= nums[p2]:
                p2 = p2 -1
            nums[p1] , nums[p2] = nums[p2] , nums[p1]
        i =  p1 + 1
        j = n-1
        while i < j:
            nums[i] , nums[j] = nums[j] , nums[i]
            i = i + 1
            j = j - 1
        return nums
        
        

        return nums
if __name__ == '__main__':
    nums = [1, 5, 1]
    obj = Solution()
    result = obj.nextPermutation(nums)
    print(result)
