class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs at every node and a common visited set
        visited = set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        res = 0

        def bfs(row: int, col: int) -> None:
            nonlocal directions
            if grid[row][col] == '0':
                visited.add((row, col))
                return

            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                for direction in directions:
                    nr, nc = direction
                    row, col = r + nr, c + nc
                    if (len(grid) > row >= 0 and len(grid[0]) > col >= 0) and (row, col) not in visited and grid[row][col] == '1':
                        q.append((row, col))
                    visited.add((row, col))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        
        return res
