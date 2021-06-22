from collections import defaultdict
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        s_dict = defaultdict(list)
        for i in range(len(s)):
            s_dict[s[i]].append(i)
        result = 0
        for word in words:
            if (self.isSubSequence(s_dict,word)):
                result += 1
        return result
    def isSubSequence(self,s_dict,word):
        j = 0
        print(word)
        for i in range(len(word)):
            check = s_dict[word[i]]
            #print("Word : {0} elements : {1}".format(word[i],check))
            if len(check) == 0:
                return False
            j = self.checkGreater(j,check)
            if j == -1:
                return False
            j += 1
        return True

    def checkGreater(self,j, check):
        for e in check:
            if e >= j:
                return e
        return -1

        



print(Solution().numMatchingSubseq("dsahjpjauf", [
      "ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))
