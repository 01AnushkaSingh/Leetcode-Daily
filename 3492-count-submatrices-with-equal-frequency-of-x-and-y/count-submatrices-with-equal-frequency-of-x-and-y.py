class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
      
        rows, cols = len(grid), len(grid[0])
      
        prefix_sum = [[[0] * 2 for _ in range(cols + 1)] for _ in range(rows + 1)]
      
        result_count = 0
      
        
        for row_idx, row_data in enumerate(grid, 1):
            for col_idx, cell_value in enumerate(row_data, 1):
               
                prefix_sum[row_idx][col_idx][0] = (prefix_sum[row_idx - 1][col_idx][0] + 
                                                   prefix_sum[row_idx][col_idx - 1][0] - 
                                                   prefix_sum[row_idx - 1][col_idx - 1][0])
              
                prefix_sum[row_idx][col_idx][1] = (prefix_sum[row_idx - 1][col_idx][1] + 
                                                   prefix_sum[row_idx][col_idx - 1][1] - 
                                                   prefix_sum[row_idx - 1][col_idx - 1][1])
              
                
                if cell_value != ".":
                  
                    character_type = ord(cell_value) & 1
                    prefix_sum[row_idx][col_idx][character_type] += 1
              
                
                if (prefix_sum[row_idx][col_idx][0] > 0 and 
                    prefix_sum[row_idx][col_idx][0] == prefix_sum[row_idx][col_idx][1]):
                    result_count += 1
      
        return result_count