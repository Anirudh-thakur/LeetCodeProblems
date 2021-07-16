class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        def numDecodingsHelper(previous,current,s,n):
            if current == n-1:
                if s[current] == '*':
                    if previous == -1:
                        return 9
                    else :
                        return 6


print(Solution().numDecodings("2*"))
