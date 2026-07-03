from collections import defaultdict
import heapq

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        
       
        graph = defaultdict(list)
        all_costs = set()
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                graph[u].append((v, cost))
                all_costs.add(cost)
                
        if not all_costs:
            return -1
            
    
        sorted_costs = sorted(list(all_costs))
        
        def can_reach_with_min_cost(min_edge_allowed: int) -> bool:
            
            pq = [(0, 0)]
            min_dist = {i: float('inf') for i in range(n)}
            min_dist[0] = 0
            
            while pq:
                curr_cost, u = heapq.heappop(pq)
                
                if u == n - 1:
                    return curr_cost <= k
                
                if curr_cost > min_dist[u]:
                    continue
                    
                for v, cost in graph[u]:
                
                    if cost >= min_edge_allowed:
                        next_cost = curr_cost + cost
                        if next_cost < min_dist[v] and next_cost <= k:
                            min_dist[v] = next_cost
                            heapq.heappush(pq, (next_cost, v))
                            
            return min_dist[n - 1] <= k


        left, right = 0, len(sorted_costs) - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            candidate_cost = sorted_costs[mid]
            
            if can_reach_with_min_cost(candidate_cost):
                ans = candidate_cost  
                left = mid + 1
            else:
                right = mid - 1
                
        return ans