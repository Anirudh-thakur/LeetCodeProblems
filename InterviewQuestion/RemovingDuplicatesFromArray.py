#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0 or n == 1:
            return n
        i = 0
        j =1 
        while j < n:
            print(nums)
            print(i)
            print(j)
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
            j+=1
        print(nums)
        return i+1
if __name__ == "__main__":
    objS = Solution()
    print(objS.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
