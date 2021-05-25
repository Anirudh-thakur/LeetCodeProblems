#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

from collections import defaultdict
class Solution(object):
    def ZDefault(self):
        return 0
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 < len2:
            return self.intersectUtil(nums1,nums2)
        else:
            return self.intersectUtil(nums2,nums1)
    def intersectUtil(self,nums1,nums2):
        dict_num = defaultdict(self.ZDefault)
        for num in nums1:
            dict_num[num] = dict_num[num] + 1
        result = []
        for num in nums2:
            if dict_num[num] != 0:
                result.append(num)
                dict_num[num]-=1
        return result
if __name__ == "__main__":
    objS = Solution()
    print(objS.intersect([1,2,2,1,2],[2,2]))