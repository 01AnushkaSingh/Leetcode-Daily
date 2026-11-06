class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        from collections import Counter


        logs.sort(key=lambda item: item[1])
        
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        active_servers = Counter()
        
        left = 0
        right = 0
        
        for original_idx, query_time in sorted_queries:
            while right < len(logs) and logs[right][1] <= query_time:
                server_id = logs[right][0]
                active_servers[server_id] += 1
                right += 1
                
            while left < len(logs) and logs[left][1] < query_time - x:
                server_id = logs[left][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                left += 1
            
            ans[original_idx] = n - len(active_servers)
            
        return ans
