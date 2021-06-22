#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3777/
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []      
        for i in range(0, len(words)):
            for j in range(i+1,len(words)):
                if self.isPallin(words[i] , words[j]):
                    result.append([i,j])
                if self.isPallin(words[j], words[i]):
                    result.append([j,i])
        return result
    def isPallin(self,w1,w2):
        test = w1+w2
        start = 0
        end = len(test)-1
        while(start < end):
            if test[start] != test[end]:
                return False
            start += 1
            end -=1
        return True
        

print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))