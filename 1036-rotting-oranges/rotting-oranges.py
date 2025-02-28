class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        queue = deque() # Will have position of rotten one
        fresh = 0
        mins = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue:
            row, col, time = queue.popleft()
            mins = time

            for r,c in directions:
                newRow, newCol = row+r, col+c

                if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    fresh -= 1
                    queue.append((newRow, newCol, time+1))

        return mins if fresh ==0 else -1 