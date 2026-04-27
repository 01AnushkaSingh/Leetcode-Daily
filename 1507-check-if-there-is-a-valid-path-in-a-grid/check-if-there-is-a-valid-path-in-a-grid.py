class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
       
        rows, cols = len(grid), len(grid[0])
      
       
        parent = list(range(rows * cols))
      
        def find(node: int) -> int:
          
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]
      
        def connect_left(row: int, col: int) -> None:
       
            if col > 0 and grid[row][col - 1] in (1, 4, 6):
                current_root = find(row * cols + col)
                left_root = find(row * cols + col - 1)
                parent[current_root] = left_root
      
        def connect_right(row: int, col: int) -> None:
            
            if col < cols - 1 and grid[row][col + 1] in (1, 3, 5):
                current_root = find(row * cols + col)
                right_root = find(row * cols + col + 1)
                parent[current_root] = right_root
      
        def connect_up(row: int, col: int) -> None:
          
            if row > 0 and grid[row - 1][col] in (2, 3, 4):
                current_root = find(row * cols + col)
                up_root = find((row - 1) * cols + col)
                parent[current_root] = up_root
      
        def connect_down(row: int, col: int) -> None:

            if row < rows - 1 and grid[row + 1][col] in (2, 5, 6):
                current_root = find(row * cols + col)
                down_root = find((row + 1) * cols + col)
                parent[current_root] = down_root
      

        for row in range(rows):
            for col in range(cols):
                street_type = grid[row][col]
              
             
                if street_type == 1:  
                    connect_left(row, col)
                    connect_right(row, col)
                elif street_type == 2:  
                    connect_up(row, col)
                    connect_down(row, col)
                elif street_type == 3:  
                    connect_left(row, col)
                    connect_down(row, col)
                elif street_type == 4: 
                    connect_right(row, col)
                    connect_down(row, col)
                elif street_type == 5: 
                    connect_left(row, col)
                    connect_up(row, col)
                else: 
                    connect_right(row, col)
                    connect_up(row, col)
      

        start_root = find(0)
        end_root = find(rows * cols - 1)
        return start_root == end_root
