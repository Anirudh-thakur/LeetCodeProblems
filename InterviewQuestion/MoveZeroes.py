#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0 
        num_Zeros = 0
        n = len(nums)
        while(i < n):
            if nums[i] != 0:
                nums[num_Zeros] = nums[i]
                num_Zeros += 1
            i+=1
        for i in range(num_Zeros,n):
            nums[i] = 0
        print(nums)            
            


if __name__ == "__main__":
    ObjS = Solution()
    print(ObjS.moveZeroes([0, 1, 0, 3, 12]))
