#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3755/

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            print(stack)
            print(token)
            try:
                int(token)
                stack.append(int(token))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.performOperation(num1,num2,token))
        return int(stack[0])
    def performOperation(self,num1,num2,token):
        if token == "+":
            return num1+num2
        elif token == "-":
            return num1 - num2
        elif token == "*":
            return num1 * num2
        else:
            result = num1/num2
            return(int(result))  
if __name__ == "__main__":
    ObjS = Solution()
    print(ObjS.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
