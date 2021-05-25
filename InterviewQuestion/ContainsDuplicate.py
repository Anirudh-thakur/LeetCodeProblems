#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

from collections import defaultdict

class Solution(object):
    def def_value(self):
        return 0
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        key_array = defaultdict(self.def_value)
        for num in nums:
            key_array[num] = key_array[num] + 1
            if key_array[num] > 1:
                return True
        return False

if __name__ == "__main__":
    ObjS = Solution()
    print(ObjS.containsDuplicate([1,2,3]))
