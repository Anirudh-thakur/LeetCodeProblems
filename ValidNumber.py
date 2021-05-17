#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3744/

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if "INF" in s.upper():
            return False
        n = len(s) - 1
        checke = s.find('e')
        checkE = s.find('E')
        if checke == 0 or checke == n:
            return False
        if checkE == n or checkE == 0:
            return False
        if abs(checke - checkE) == 1:
            return False
        if checke != -1:
            try:
                int(s[checke+1 : n+1])
                s = s[0 : checke]
            except ValueError:
                return False
        if checkE != -1:
            try:
                int(s[checkE+1 : n+1])
                s = s[0: checkE]
            except ValueError:
                return False 
        
        try:
            float(s)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    objS = Solution()
    result = objS.isNumber("-inf")
    print(result)
