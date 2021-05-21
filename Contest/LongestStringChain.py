#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3746/

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 1:
            return 1
        words = list(set(words))
        chain_hash = {}
        word_hash = {}
        for word in words:
            key = len(word)
            word_hash[word] = 1
            if key in chain_hash.keys():
                add = chain_hash[key]
                add.append(word)
                chain_hash[key] = add
            else:
                chain_hash[key] = [word]

        keys = sorted(chain_hash.keys())
   #     print(keys)
        check = len(keys)
        if check == 1:
            return 1
        max = 1
        for i in range(len(keys) - 1):
            for key1 in chain_hash[keys[i]]:
               # print(key1)
                for key2 in chain_hash[keys[i+1]]:
                   # print(key2)
                    if len(key1)+1 == len(key2) and self.isSimilar(key1,key2):
                        add_max = word_hash[key1] + 1
                        if add_max > word_hash[key2]:
                            word_hash[key2] = add_max
                    #    print(word_hash[key2])
                        if word_hash[key2] == check:
                            return word_hash[key2]
        max = 1
  #      print("test")
        for word in words:
            if word_hash[word] > max:
                max = word_hash[word]
        return max
            
    def isSimilar(self,key1,key2):
        n = len(key1)
        j = 0
 #       print(key1)
 #       print(key2)
 #       print(n)
        for c in key2:
            if c == key1[j]:
                j = j + 1
            if j == n:
                return True
        return False



if __name__ == '__main__':
    words = ["a", "ab", "ac", "bd", "abc", "abd", "abdd"]
    objS = Solution()
    result = objS.longestStrChain(words)
    print(result)
