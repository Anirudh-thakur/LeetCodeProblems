class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0;
        if target <= nums[0]:
            return 0
        n = len(nums)
        if target > nums[n-1]:
            return n
        if target == nums[n-1]:
            return n-1
        min = 0
        if abs(target-nums[0]) <= abs(target-nums[n-1]):
                result = 1
                min = abs(target-nums[0])
        else:
            result = n-1
            min = abs(target-nums[n-1])
        start = 0
        end = n-1
        while start < end:
            mid = int((start + end)/2)
            print("Mid Pointer:"+str(mid))
            print("Mid element:"+str(nums[mid]))
            print("Minimum differnce:"+str(min))
            print("New Min dif:"+str(abs(nums[mid]-target)))
            print("result:"+str(result))
            if(abs(nums[mid]-target) < min):
                min = abs(nums[mid]-target)
                if nums[mid] < target:
                    result = mid+1
                elif nums[mid] > target:
                    result = mid
                else:
                    result = mid
                    break
            if target < nums[mid]:
                end = mid
            else:
                start = mid+1
        return result
if __name__ == '__main__':
    nums = [1, 3, 4, 5, 6]
    target = 3
    obj = Solution()
    result = obj.searchInsert(nums, target)
    print(result)

