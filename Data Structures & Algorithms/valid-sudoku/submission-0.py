# then check each row
# then check each column
# then check each box

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        
        # checking each row
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in nums and board[i][j] in seen:
                    return False
                elif board[i][j] != ".":
                    seen.add(board[i][j])
        
        # checking each column
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in nums and board[j][i] in seen:
                    return False
                elif board[j][i] != ".":
                    seen.add(board[j][i])
            
        # checking each box (1, 1 ; 1, 4; 1, 7; 4, x; 7, x)
        for i in range(1, 8, 3):
            for j in range(1, 8, 3):
                seen = set()
                directions = [[0, 0], [-1, -1], [0, -1], [+1, -1], [+1, 0], [+1, +1], [0, +1], [-1, +1], [-1, 0]]
                for x, y in directions:
                    new_x, new_y = x + i, y + j
                    if board[new_x][new_y] in nums and board[new_x][new_y] in seen:
                        return False
                    elif board[new_x][new_y] != ".":
                        seen.add(board[new_x][new_y])
        
        return True
