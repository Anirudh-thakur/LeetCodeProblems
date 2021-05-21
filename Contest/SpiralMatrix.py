#https://leetcode.com/problems/spiral-matrix/
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        right = len(matrix[0])-1
        left = 0
        top = 0
        bottom = len(matrix)-1
        flag = 0
        while left<=right and top<=bottom:
                if flag == 0:
                    for i in range(left,right+1):
                        result.append(matrix[top][i])
                    top = top + 1
                    flag =1
                elif flag == 1:
                    for i in range(top,bottom+1):
                        result.append(matrix[i][right])
                    right = right -1
                    flag =2
                elif flag == 2:
                    for i in range(right,left-1,-1):
                        result.append(matrix[bottom][i])
                    bottom = bottom-1
                    flag = 3
                else:
                    for i in range(bottom,top-1,-1):
                        result.append(matrix[i][left])
                    left = left + 1
                    flag = 0
            
        return result

if __name__ == '__main__':
    matrix = matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    obj = Solution()
    result = obj.spiralOrder(matrix)
    print(result)