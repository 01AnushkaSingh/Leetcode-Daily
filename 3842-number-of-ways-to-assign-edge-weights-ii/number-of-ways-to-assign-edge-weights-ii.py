import math

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

       
        LOG = math.ceil(math.log2(n))
        up = [[0] * (LOG + 1) for _ in range(n + 1)]
        depth = [0] * (n + 1)

        def dfs(node, p, d):
            depth[node] = d
            up[node][0] = p
            for i in range(1, LOG + 1):
                up[node][i] = up[up[node][i - 1]][i - 1]
            for neighbor in adj[node]:
                if neighbor != p:
                    dfs(neighbor, node, d + 1)

        dfs(1, 1, 0)

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG + 1):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        def get_distance(u, v):
            lca = get_lca(u, v)
            return depth[u] + depth[v] - 2 * depth[lca]

        ans = []
        MOD = 1_000_000_007

    
        power_of_2 = [1] * (n + 1)
        for i in range(1, n + 1):
            power_of_2[i] = (power_of_2[i - 1] * 2) % MOD

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            
            dist = get_distance(u, v)
           
            ways = power_of_2[dist - 1]
            ans.append(ways)

        return ans