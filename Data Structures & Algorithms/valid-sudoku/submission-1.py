from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] in nums and (board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[((row // 3) * 3) + (col // 3)]):
                    return False
                elif board[row][col] != ".":
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    boxes[((row // 3) * 3) + (col // 3)].add(board[row][col])
        
        return True
