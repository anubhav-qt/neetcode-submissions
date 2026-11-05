class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited, islands = set(), 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(row: int, col: int) -> None:
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                for direction in directions:
                    temp_r, temp_c = direction
                    new_row, new_col = r + temp_r, c + temp_c
                    if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])) and ((new_row, new_col) not in visited) and (grid[new_row][new_col] == '1'):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == '1':
                    bfs(row, col)
                    islands += 1

        return islands
