#https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check = [0 for i in range(10)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                data = int(board[i][j])
                if(check[data] == 1):
                    return False
                else:
                    check[data] = 1
            check = [0 for i in range(10)]
        for i in range(9):
            for j in range(9):
                if board[j][i] == '.':
                    continue
                data = int(board[j][i])
                if(check[data] == 1):
                    return False
                else:
                    check[data] = 1
            check = [0 for i in range(10)]
        for k in range(0,9,3):
            for l in range(0,9,3):    
                for i in range(k,k+3,1):
                   # print()
                    for j in range(l,l+3,1):
                       # print(board[i][j],end=" ")
                        if board[i][j] == '.':
                             continue
                        data = int(board[i][j])
                        if(check[data] == 1):
                            return False
                        else:
                            check[data] = 1
                check = [0 for i in range(10)]
                #print(check)        
        result = True
        return result

if __name__ == '__main__':
    board = [[".",".",".",".","5",".",".","1","."],
             [".","4",".","3",".",".",".",".","."],
             [".",".",".",".",".","3",".",".","1"],
             ["8",".",".",".",".",".",".","2","."],
             [".",".","2",".","7",".",".",".","."],
             [".","1","5",".",".",".",".",".","."],
             [".",".",".",".",".","2",".",".","."],
             [".","2",".","9",".",".",".",".","."],
             [".",".","4",".",".",".",".",".","."]]
    obj = Solution()
    result = obj.isValidSudoku(board)
    print(result)
