from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
     
        A = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        
        A.sort(key=lambda x: x[1])
        n = len(A)
        
        ends = [x[1] for x in A]
        
      
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            l, r, w, idx = A[i - 1]
            
            
            p = bisect_right(ends, l - 1, 0, i - 1)
            
            for k in range(1, 5):
                w1, path1 = dp[i - 1][k]
                
                w2, path2 = dp[p][k - 1]
                w2 += w
                new_path = sorted(path2 + [idx])
                
                if w1 > w2:
                    dp[i][k] = (w1, path1)
                elif w2 > w1:
                    dp[i][k] = (w2, new_path)
                else:
                    if path1 < new_path:
                        dp[i][k] = (w1, path1)
                    else:
                        dp[i][k] = (w2, new_path)
                        
        return dp[n][4][1]
