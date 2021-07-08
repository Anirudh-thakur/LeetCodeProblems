class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        Combined = self.getStrainghtArray(matrix,n)
        return Combined[k-1]

    def getStrainghtArray(self,matrix,n):
        result = matrix[0]
        if n == 1:
            return result
        for i in range(1,n):
            temp = []
            m = len(result)
            p1 = 0;p2 = 0;
            while p1 < m and p2 < n:
                if result[p1] < matrix[i][p2]:
                    temp.append(result[p1])
                    p1 += 1
                else:
                    temp.append(matrix[i][p2])
                    p2 += 1 
            while p1 < m:
                temp.append(result[p1])
                p1 += 1
            while p2 < n:
                temp.append(matrix[i][p2])
                p2 += 1
            result = list(temp)
        return result 

        
print(Solution().kthSmallest(matrix= [[-5]], k = 1));
