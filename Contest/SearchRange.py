#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1,-1]
        n = len(nums)
 #       print(n)
        if(n == 0):
 #           print("check1")
            return result
        if(target<nums[0] or target > nums[n-1]):
 #           print("check2")
            return result
        start = 0
        end = n-1
        flag = 0
        while(start<=end):
            mid = int(((start+end)/2))
            print(mid)
            if nums[mid] == target:
                flag = 1
                break
            elif target < nums[mid]:
                end = mid-1
            else:
                start = mid+1 
        if flag == 0:
  #          print("check3")
            return result
        top = mid
        bottom = mid
 #       print(mid)
        while(top < n and nums[top] == target) :
            top = top + 1
        while(bottom >=0 and nums[bottom] == target):
            bottom = bottom - 1
        result[0] = bottom +1
        result[1] = top -1
        return result
if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 6
    obj = Solution()
    result = obj.searchRange(nums,target)
    print(result)