#https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3753/
import itertools
from collections import defaultdict
import sys
import difflib
class Solution(object):
    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words)
        if n == 1:
            return words[0]
        word_perm = list(itertools.permutations(words))
        dyn = defaultdict()
        for i in range(n):
            for j in range(n):
                if i !=j:
                    dyn[(words[i],words[j])] = self.getWordCombine(words[i],words[j])
        #            print(words[i])
        #            print(words[j])
        #            print(dyn[(words[i],words[j])])
#        print(word_perm)
        minLen = sys.maxsize
        result = ""
        pm = len(word_perm)
        for p in range(pm):
            check = dyn[(word_perm[p][0],word_perm[p][1])]
            #print("check:"+str(check))
            #print(word_perm[p])
            for i in range(2,n):
            #    print(word_perm[p][i])
            #    print(word_perm[p][i+1])
            #    m = len(word_perm[p][i])
                #check = dyn[(check, word_perm[p][i])]
                check = self.getWordCombine(check,word_perm[p][i])
            #    print("Add:"+add)

            #print(check)
            if len(check) < minLen:
                minLen = len(check)
                result = check
        test = ["gcta", "ctaagt", "ttca", "catg", "atgcatc"]
        print(test)
        check = dyn[(test[0],test[1])]
        for i in range(2, n):
            print("check:"+str(check))
            print(test[i])
            #    print(word_perm[p][i])
            #    print(word_perm[p][i+1])
            #    m = len(word_perm[p][i])
            #check = dyn[(check, word_perm[p][i])]
            check = self.getWordCombine(check, test[i])
            #    print("Add:"+add)

            #print(check)
        print(check)
        return result
        
    def getWordCombine(self,word1,word2):
       result = difflib.SequenceMatcher(None, word1,word2)
       n = len(word1)
       m = len(word2)
       pos_a, pos_b, size = result.find_longest_match(0, n, 0, m)
       if pos_a+size == n:
           return word1 + word2[size:]
        if pos_b+size == m:
            return word1[0:pos_a] + word2
       return word1 + word2
if __name__ == '__main__':
    ObjS = Solution()
    print(ObjS.shortestSuperstring(
        ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
