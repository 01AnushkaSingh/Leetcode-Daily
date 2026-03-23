class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        MOD = 10**9 + 7

   
        dp_max = [[0] * cols for _ in range(rows)]
        dp_min = [[0] * cols for _ in range(rows)]

        dp_max[0][0] = dp_min[0][0] = grid[0][0]

    
        for i in range(1, rows):
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]

      
        for j in range(1, cols):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
              
                val1 = dp_max[i-1][j] * grid[i][j]
                val2 = dp_min[i-1][j] * grid[i][j]
                val3 = dp_max[i][j-1] * grid[i][j]
                val4 = dp_min[i][j-1] * grid[i][j]

                dp_max[i][j] = max(val1, val2, val3, val4)
                dp_min[i][j] = min(val1, val2, val3, val4)

        max_prod = dp_max[rows - 1][cols - 1]
        if max_prod >= 0:
            return max_prod % MOD
        else:
            return -1