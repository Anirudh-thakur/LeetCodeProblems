class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        dyn = [[0 for _ in range(m+1)] for _ in range(n+1)]
        result = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1] == nums2[j-1]:
                    dyn[i][j] = dyn[i-1][j-1]+1
                if dyn[i][j] > result:
                    result = dyn[i][j]

        return result


print(Solution().findLength([1, 2, 3, 2, 1],[3, 2, 1, 4]))
