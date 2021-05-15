#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3737/

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        target.sort()
        #print(target)
        l = len(target)
        if l == 1 :
            if target[l-1] == 1:
                return True
            else:
                return False
        #print(l)
        numOfOnes = 0;
        sum = 0
        nTarget = []
        for x in target:
 #           print(x)
            if x == 1:
                numOfOnes = numOfOnes + 1
            else :
                nTarget.append(x)
 #       print(numOfOnes)
 #       print(nTarget)
        target = nTarget
        n = len(target)

        if numOfOnes == l-1 and numOfOnes != 0:
            print("check")
            if numOfOnes != 1:
                if target[n-1] % numOfOnes == 1 :
                    return True;
                else:
                    return False;
            else:
                return True;
 #       print(target)
 #       print(numOfOnes)
        while l!=numOfOnes :
 #           print("number of ones:"+str(numOfOnes))
            sum = 0
            n = len(target)
            if(n == 0):
                break
            for i in range(n-1):
                sum = sum+target[i]
            sum = sum + numOfOnes
 #           print("sum:"+str(sum))
            if(target[n-1] == 1):
                return True
            target[n-1] = target[n-1] - sum
 #           print("Target:"+str(target[n-1]))
            if target[n-1] <= 0 :
                return False;
            if target[n-1] == 1:
                numOfOnes = numOfOnes + 1
                target.remove(target[n-1])
            else:
                target[n-1] = target[n-1] % sum
  #              print("Target mod:"+str(target[n-1]))
                if target[n-1] == 1:
                    numOfOnes = numOfOnes + 1
                    target.remove(target[n-1])
                elif target[n-1] == 0:
                    return False
            target.sort()
           # print(target)


        return True

if __name__ == '__main__':
    obj = Solution()
    target = [1, 1, 1, 1, 11, 16]
    result = obj.isPossible(target)
    print(result)
