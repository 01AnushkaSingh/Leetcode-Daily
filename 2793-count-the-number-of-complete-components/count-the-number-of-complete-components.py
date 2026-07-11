from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
       
      
        def dfs(node: int) -> tuple[int, int]:
           
            visited[node] = True
          
           
            vertex_count = 1
            edge_count = len(adjacency_list[node])
          
            
            for neighbor in adjacency_list[node]:
                if not visited[neighbor]:
                  
                    vertices, edges = dfs(neighbor)
                    vertex_count += vertices
                    edge_count += edges
          
            return vertex_count, edge_count
      
       
        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
      
       
        visited = [False] * n
      
        
        complete_component_count = 0
      
        
        for vertex in range(n):
            if not visited[vertex]:
               
                vertices, edges = dfs(vertex)
              
               
                if vertices * (vertices - 1) == edges:
                    complete_component_count += 1
      
        return complete_component_count
