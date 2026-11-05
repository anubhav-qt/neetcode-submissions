# traverse and dfs at each node
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res, char_index = False, 0
        visited = set()

        def dfs(row: int, col: int, char_index: int) -> None:
            if self.res:
                return
            
            if char_index == len(word):
                self.res = True
                return
            
            if row >= len(board) or row < 0 or 0 > col or col >= len(board[0]):
                return
            
            if char_index < len(word) and board[row][col] != word[char_index]:
                return

            # if same char
            if (row, col) not in visited:
                visited.add((row, col))
                dfs(row + 1, col, char_index + 1)
                dfs(row - 1, col, char_index + 1)
                dfs(row, col + 1, char_index + 1)
                dfs(row, col - 1, char_index + 1)
                if not self.res:
                    visited.remove((row, col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.res:
                    return True
                dfs(i, j, 0)

        return self.res
