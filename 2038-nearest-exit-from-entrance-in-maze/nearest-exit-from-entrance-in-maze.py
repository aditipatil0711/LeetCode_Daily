class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m,n = len(maze), len(maze[0])

        queue = deque([(entrance[0],entrance[1],0)])
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            row,col,steps = queue.popleft()
            for r,c in directions:
                newRow, newCol = row + r, col + c
                if 0 <= newRow <m and 0 <=   newCol < n and maze[newRow][newCol] == '.':
                    if newRow == 0 or newRow == m-1 or newCol == 0 or newCol == n-1:
                        return steps+1
                    maze[newRow][newCol] = '+'
                    queue.append((newRow, newCol, steps+1))
        return -1