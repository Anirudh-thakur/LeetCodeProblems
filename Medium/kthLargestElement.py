#https: // leetcode.com/problems/kth-largest-element-in-an-array/
from heapq import heapify,heappop
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #nums = [num*-1 for num in nums]
        heapify(nums)
        return heapq.nlargest(k, nums)[k-1]
if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    ObjS = Solution()
    result = ObjS.findKthLargest(nums,k)
    print(result)
