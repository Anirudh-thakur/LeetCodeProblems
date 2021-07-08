#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3794/
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for let in s:
            if stack and stack[-1] == let:
                stack.pop()
            else:
                stack.append(let)

        return ''.join(stack) 
        

print(Solution().removeDuplicates("azxxzy"))
