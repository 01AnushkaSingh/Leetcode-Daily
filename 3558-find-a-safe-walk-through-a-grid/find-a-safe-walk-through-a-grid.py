from collections import deque
from typing import List
from math import inf
from itertools import pairwise


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
     
        rows, cols = len(grid), len(grid[0])
      
        
        distance = [[inf] * cols for _ in range(rows)]
      
        
        distance[0][0] = grid[0][0]
      
       
        queue = deque([(0, 0)])
      
     
        directions = (-1, 0, 1, 0, -1)
      
      
        while queue:
            current_x, current_y = queue.popleft()

            for delta_x, delta_y in pairwise(directions):
                next_x = current_x + delta_x
                next_y = current_y + delta_y
              
          
                if (0 <= next_x < rows and 
                    0 <= next_y < cols and 
                    distance[next_x][next_y] > distance[current_x][current_y] + grid[next_x][next_y]):
                  
               
                    distance[next_x][next_y] = distance[current_x][current_y] + grid[next_x][next_y]
                  
                 
                    queue.append((next_x, next_y))
      
       
        return distance[-1][-1] < health