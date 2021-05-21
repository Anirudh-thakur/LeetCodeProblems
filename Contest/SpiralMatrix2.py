#https://leetcode.com/problems/spiral-matrix-ii/

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)] for i in range(n)]
        add = 1
        flag = 0
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        while(left<=right and top<=bottom):
            if flag == 0:
                for i in range(left,right+1):
                    result[top][i] = add
                    add = add + 1
                flag = 1
                top = top+1
            elif flag == 1:
                for i in range(top,bottom+1):
                    result[i][right] = add 
                    add = add+1
                flag = 2
                right = right-1
            elif flag == 2:
                for i in range(right,left-1,-1):
                    result[bottom][i] = add
                    add = add+1
                flag = 3
                bottom = bottom-1
            else:
                for i in range(bottom,top-1,-1):
                    result[i][left] = add
                    add = add+1
                flag = 0
                left = left+1


        return result
if __name__ == '__main__':
    obj = Solution()
    result = obj.generateMatrix(3)
    print(result)