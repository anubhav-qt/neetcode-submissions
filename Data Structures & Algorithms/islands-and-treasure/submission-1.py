class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            r, c = q.popleft()
            
            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
