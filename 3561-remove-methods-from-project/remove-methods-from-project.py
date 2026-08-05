from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        
        
        suspicious = [False] * n
        queue = deque([k])
        suspicious[k] = True
        
        while queue:
            curr = queue.popleft()
            for nxt in graph[curr]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    queue.append(nxt)
        
        
        can_remove = True
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                can_remove = False
                break
        
       
        if can_remove:
            return [i for i in range(n) if not suspicious[i]]
        else:
            return list(range(n))