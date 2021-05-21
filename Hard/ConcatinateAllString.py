#https://leetcode.com/problems/substring-with-concatenation-of-all-words/
import itertools
import re
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l1 = len(words[0])
        l2 = len(words)
        n = len(s)
        if l1*l2 > n:
            return []
        word_perm = list(itertools.permutations(words))
        word_string =set()
        for word in word_perm:
            temp = ""
            for val in word:
                temp = temp+val
            word_string.add(temp)
        result = []
        for word in word_string:
            if word in s:
                print(word)
                print(s)
                for m in re.finditer(word, s):
                    result.append(m.start())
        return result

if __name__ == '__main__':
    s = "aaa"
    words = ["a", "a"]
    ObjS = Solution()
    result = ObjS.findSubstring(s,words)
    print(result)
