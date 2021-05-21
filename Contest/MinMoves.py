#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3748/

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        if n % 2 != 0:
            mid = int(n/2)
  #          print(mid)
            return sum([abs(num-nums[mid]) for num in nums])
        else:
            mid1 = int(n/2)
            mid2 = int(n/2)-1
            sum1 = sum([abs(num-nums[mid1]) for num in nums])
            sum2 = sum([abs(num-nums[mid2]) for num in nums])
            return min(sum1,sum2)

        
if __name__ == '__main__':
    nums = [1, 0, 0, 8, 6]
    ObjS = Solution()
    result = ObjS.minMoves2(nums)
    print(result)
