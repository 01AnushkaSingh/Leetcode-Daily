class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        from functools import lru_cache


        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dfs(i, j, direction):
            if i == m - 1 and j == n - 1:
                return 1
            
            if grid[i][j] == 1:
                if direction == 0:  
                    if i + 1 < m:
                        return dfs(i + 1, j, 1)
                elif direction == 1: 
                    if j + 1 < n:
                        return dfs(i, j + 1, 0)
                return 0  
            
            paths = 0
            
            if j + 1 < n:
                paths = (paths + dfs(i, j + 1, 0)) % MOD
                
            if i + 1 < m:
                paths = (paths + dfs(i + 1, j, 1)) % MOD
                
            return paths

        return dfs(0, 0, -1)
