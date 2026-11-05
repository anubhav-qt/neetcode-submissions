class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(row: int, col: int) -> None:
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            q = deque([(row, col)])
            level = 0

            while q:
                level += 1
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for direction in directions:
                        nr, nc = r + direction[0], c + direction[1]
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                            if grid[nr][nc] != 0 and grid[nr][nc] != -1 and level < grid[nr][nc]:
                                grid[nr][nc] = level
                                q.append((nr, nc))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    bfs(row, col)
