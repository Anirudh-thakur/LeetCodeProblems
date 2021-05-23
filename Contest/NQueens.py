#https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3752/

class Solution(object):
    def __init__(self):
        self.result = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        bS = "." * n
        board = [bS for i in range(n)]
        self.solveNQueensUtil(board,n,0)
        return self.result

    def solveNQueensUtil(self, board, n, row):
        #print(self.result)
        if row == n:
            print(board)
            temp = list(board)
            self.result.append(temp)
            return 
        for col in range(n):
            if self.checkQConditions(row,col,board,n):
                board[row] = board[row][0:col]+'Q'+board[row][col+1:n]
                #print(board[row])
                self.solveNQueensUtil(board,n,row+1)
                board[row] = board[row][0:col]+'.'+board[row][col+1:n]
    def checkQConditions(self,row,col,board,n):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i , j = row,col
        while i>=0 and j>=0 :
            if board[i][j] == 'Q':
                return False
            i-=1;j-=1
        i, j = row, col
        while(i >= 0  and j < n):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
if __name__ == "__main__":
    ObjS = Solution()
    result = ObjS.solveNQueens(4)
    print(result)
