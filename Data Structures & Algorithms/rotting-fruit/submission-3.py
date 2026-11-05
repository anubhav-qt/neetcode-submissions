class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        level = -1
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0

        # fill the queue with all rotten oranges
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        # run the bfs
        while q:
            level += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for direction in directions:
                    rd, cd = direction
                    nr, nc = r + rd, c + cd

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1

        return level if fresh == 0 else -1
