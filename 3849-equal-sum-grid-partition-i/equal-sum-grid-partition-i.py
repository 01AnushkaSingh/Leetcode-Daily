class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        total_sum = sum(sum(row) for row in grid)
      
        
        if total_sum % 2:
            return False
      
       
        target_sum = total_sum // 2
      
    
        prefix_sum = 0
        for i, row in enumerate(grid):
            prefix_sum += sum(row)
           
            if prefix_sum == target_sum and i != len(grid) - 1:
                return True
      
        prefix_sum = 0
  
        for j, column in enumerate(zip(*grid)):
            prefix_sum += sum(column)
            
            if prefix_sum == target_sum and j != len(grid[0]) - 1:
                return True
     
        return False