class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.invalid_cols = set()
        self.invalid_negative_diagonals = set() # row - col is same for all in same negative diagonal
        self.invalid_positive_diagonals = set() # row + col is same for all in same positive diagonal
        self.solution = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row: int) -> None:
            if row >= n:
                self.res.append([''.join(r) for r in self.solution])
                return

            for col in range(n):
                if col not in self.invalid_cols:
                    if (row - col) not in self.invalid_negative_diagonals and (row + col) not in self.invalid_positive_diagonals:
                        self.solution[row][col] = 'Q'
                        self.invalid_cols.add(col)
                        self.invalid_negative_diagonals.add(row - col)
                        self.invalid_positive_diagonals.add(row + col)
                        backtrack(row + 1)
                        self.solution[row][col] = '.'
                        self.invalid_cols.remove(col)
                        self.invalid_negative_diagonals.remove(row - col)
                        self.invalid_positive_diagonals.remove(row + col)
        
        backtrack(0)
        return self.res
