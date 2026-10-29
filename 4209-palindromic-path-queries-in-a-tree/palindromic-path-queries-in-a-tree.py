
from collections import defaultdict
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOGN = 17
        up = [[0] * LOGN for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        root_mask = [0] * n 
        char_values = [1 << (ord(c) - ord('a')) for c in s]
        
      
        stack = [(0, 0, char_values[0])] 
        visited = [False] * n
        visited[0] = True
        
        dfs_order = []
        
         
        def dfs(node, parent, current_mask):
            nonlocal timer
            tin[node] = timer
            timer += 1
            root_mask[node] = current_mask
            up[node][0] = parent
            for i in range(1, LOGN):
                up[node][i] = up[up[node][i-1]][i-1]
                
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, current_mask ^ char_values[neighbor])
            tout[node] = timer
            
        import sys
        sys.setrecursionlimit(200000)
        dfs(0, 0, char_values[0])
        
        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[u] >= tout[v]
            
        def get_lca(u, v):
            if is_ancestor(u, v): return u
            if is_ancestor(v, u): return v
            for i in range(LOGN - 1, -1, -1):
                if not is_ancestor(up[u][i], v):
                    u = up[u][i]
            return up[u][0]

        bit = [0] * (n + 1)
        
        def bit_update(idx, val):
            idx += 1
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx):
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        def range_xor_update(l, r, val):
            bit_update(l, val)
            bit_update(r + 1, val)

        ans = []
        curr_char_mask = list(char_values)
        
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                node = int(parts[1])
                new_char = parts[2]
                new_mask = 1 << (ord(new_char) - ord('a'))
                
                change = curr_char_mask[node] ^ new_mask
                curr_char_mask[node] = new_mask
                
                range_xor_update(tin[node], tout[node] - 1, change)
                
            else:  
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                mask_u = root_mask[u] ^ bit_query(tin[u])
                mask_v = root_mask[v] ^ bit_query(tin[v])
                mask_lca_char = curr_char_mask[lca]
                
                path_mask = mask_u ^ mask_v ^ mask_lca_char
                
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
                
        return ans
