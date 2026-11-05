class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = set()

        def dfs(row: int, col: int, char_index: int) -> bool:
            if char_index == len(word):
                return True
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return False
            if board[row][col] != word[char_index]:
                return False

            if (row, col) not in self.visited:
                self.visited.add((row, col))
                if (dfs(row + 1, col, char_index + 1) or
                    dfs(row - 1, col, char_index + 1) or
                    dfs(row, col + 1, char_index + 1) or
                    dfs(row, col - 1, char_index + 1)):
                    return True
                self.visited.remove((row, col))
            
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        
        return False
