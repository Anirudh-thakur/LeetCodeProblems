#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3750/
class Solution(object):
    def __init__(self):
        self.w_replace = []
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        n = len(pattern)
        p_freq = [ 0 ] * 26
        for i in range(n):
            p_freq[ord(pattern[i])- 97]+=1
        result = []
        for word in words:
            m = len(word)
            if m != n:
                continue
            w_freq = [ 0 ] * 26
   #         print(word)
            for i in range(n):
                w_freq[ord(word[i]) - 97] += 1
            add_flag = 0
            p_isReplaced = [0] * 26
            w_old = word
            self.w_replace = [0] * n
            for i in range(n):
                if w_freq[ord(word[i]) - 97] != p_freq[ord(pattern[i])  - 97]:
  #                  print("Check")
                    add_flag = 1
                    break
                if p_isReplaced[ord(pattern[i])-97] == 1 and pattern[i] != w_old[i]:
  #                  print("Check:"+(pattern[i]))
  #                  print("Check:"+word[i])
                    add_flag = 1
                    break
                elif p_isReplaced[ord(pattern[i])-97] == 0:
                    if pattern[i] != w_old[i]:
                        if self.w_replace[i] == 1:
                            add_flag = 1
                            break
                        w_old =  self.replace(w_old,i,n,pattern[i])#w_old[0:i]+w_old[i:n].replace(w_old[i], pattern[i])
                    p_isReplaced[ord(pattern[i])-97] = 1
 #               print(word[i])
 #               print(pattern[i])
 #               print(w_old)
 #           print(add_flag)
 #           print(w_old)
            if w_old == pattern and add_flag == 0:
                result.append(word)
 #           print(word)
        return result

    def replace(self, w_old, i, n, pattern):
        result = w_old[0:i]
        for c in range(i,n):
            if w_old[c] == w_old[i] and self.w_replace[c] != 1:
                result = result+pattern
                self.w_replace[c] = 1
            else:
                result = result+w_old[c]
        return result
if __name__ == '__main__':
    words = ["abc", "cba", "xyx", "yxx", "yyx"]

    pattern = "abc"
    ObjS = Solution()
    result = ObjS.findAndReplacePattern(words,pattern)
    print(result)
