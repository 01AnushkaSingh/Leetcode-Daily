class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
       
        def dfs(row: int, col: int) -> int:
           
            is_not_boundary = int(0 < row < rows - 1 and 0 < col < cols - 1)
          
            grid[row][col] = 1
          
            for i in range(4):
                next_row = row + directions[i]
                next_col = col + directions[i + 1]
              
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0:
                    is_not_boundary &= dfs(next_row, next_col)
          
            return is_not_boundary
      
        rows, cols = len(grid), len(grid[0])
      
      
        directions = [-1, 0, 1, 0, -1]
      
        closed_island_count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and dfs(row, col):
                    closed_island_count += 1
                  
        return closed_island_count
