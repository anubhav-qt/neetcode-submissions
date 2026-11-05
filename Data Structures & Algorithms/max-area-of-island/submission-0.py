class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited, max_area = set(), 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(row: int, col: int) -> None:
            nonlocal max_area
            q, area = deque([(row, col)]), 1
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                for direction in directions:
                    temp_r, temp_c = direction
                    nr, nc = r + temp_r, c + temp_c
                    if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and ((nr, nc) not in visited) and (grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1

            max_area = max(max_area, area)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    bfs(row, col)

        return max_area
