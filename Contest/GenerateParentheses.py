import itertools
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pair = self.getInitial(n)
        print(pair)
        all_perms = itertools.permutations(pair)
        para_set = set()
        for p in all_perms:
            add_ele = ""
            for element in p:
                add_ele = add_ele + element
            para_set.add(add_ele)
        result = []
        for para in para_set:
            if self.isValid(para):
                result.append(para)
        return result 
    def isValid(self,para):
        stack = []
        print(para)
        for br in para:
            if br == "(" :
                stack.append(br)
            else :
                if len(stack) == 0:
                    return False
                elif stack[len(stack) - 1] == "(":
                    stack.pop()
                else:
                    return False
        return True

    def getInitial(self,n):
        result = ""
        for i in range(n):
            result = result + "("
        for i in range(n):
            result = result + ")"
        return result
        

print(Solution().generateParenthesis(4))