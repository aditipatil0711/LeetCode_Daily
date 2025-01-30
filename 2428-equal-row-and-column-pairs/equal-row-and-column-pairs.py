class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(grid)

        #Row counter

        row_counter = Counter()
        for row in grid:
            row_tuple = tuple(row)
            row_counter[row_tuple] += 1 
        
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

        return count
        
        