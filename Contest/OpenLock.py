#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3767/

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends_set = set(deadends)
        if target in deadends_set:
            return -1
        queue = [["0000",0]]
        visited = {'0000'}
        while len(queue) != 0:
            (current_String,result) = queue.pop(0)
            if current_String == target:
                return result
            if current_String in deadends_set:
                continue
            for i in range(4):
                digit = int(current_String[i]) 
                for step in [-1,1]:
                    x = (digit + step) % 10
                    new_String = current_String[:i] + str(x) + current_String[i+1:]
                    if new_String not in visited:
                        queue.append([new_String, result+1])
                        visited.add(new_String)
        return -1


deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"

print(Solution().openLock(deadends,target))
