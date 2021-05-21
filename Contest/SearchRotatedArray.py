class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        end = n- 1
        start = 0
        pivot = self.getPivot(nums,start,end)
     #   print("Pivot:"+str(pivot))
        if pivot == -1:
            return self.binSearch(start,end,nums,target)
        
        if nums[pivot] == target:
            return pivot
     #   print(nums[0])
        if target >= nums[0]:
     #       print("Check")
            return self.binSearch(start,pivot-1,nums,target)
        return self.binSearch(pivot+1,end,nums,target)
    def binSearch(self,start,end,nums,target):
        while(start <= end):
            mid = int((start+end)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def getPivot(self,nums,start,end):
        if start == end:
            return start
        while start<=end:
            mid = int((start+end)/2)
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid 
            if mid > start and nums[mid] < nums[mid - 1]:
                return mid-1
            if nums[start] >= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

   
if __name__ == '__main__':
    obj = Solution()
    nums = [3,5,1]
    target = 3
    result = obj.search(nums,target)
    print(result)