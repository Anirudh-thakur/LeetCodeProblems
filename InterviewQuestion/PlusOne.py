#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 0
        for i in reversed(range(len(digits))):
            digits[i] = digits[i] + 1
            if digits[i] < 10:
                flag =1 
                break
            else:
                digits[i] = digits[i] % 10
        if flag == 0:
            digits.insert(0,1)
        return digits
if __name__ == "__main__":
    ObjS = Solution()
    print(ObjS.plusOne([9,9,9]))
