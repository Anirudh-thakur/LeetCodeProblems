#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3757/
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = list(set(words))
        n = len(words)
        if n == 1:
            return 0
        max = 0
        dyn = []
        for i in range(n):
            #convert all words to there equivalent bit string
            dyn.append(self.getLetterCount(words[i]))
        for i in range(n):
            for j in range(i+1,n):
                # to compare bit string using bitwise and operation
                if ((dyn[i] & dyn[j])== 0) and (len(words[i]) * len(words[j])) > max:
                    max = len(words[i]) * len(words[j])
        return max

    def getLetterCount(self , word):
        result = 0
        """[summary]
        converts string to binary order 
        fn(a) = 1
        fn(b) = 10 = 2
        fn(c) = 100 = 4
        fn(abc) = 1 or 10 or 100 = 111 = 7 ( or sum of pow(2,c) for all char sequence in word) 
        fn(az) = 100000000000001 or in integer : 33554433
        by using or operation and bit conversion ( pow(2,n) == 1 << n)
        """
        for w in set(word):
            result |= 1 << (ord(w) - ord('a'))
        return result

if __name__ == "__main__":
    ObjS = Solution()
    print(ObjS.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
