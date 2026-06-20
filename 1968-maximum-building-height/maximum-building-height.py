class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        
        restrictions.sort()
        
        m = len(restrictions)
        
        
        for i in range(1, m):
            idx_diff = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + idx_diff)
            
       
        for i in range(m - 2, -1, -1):
            idx_diff = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + idx_diff)
            
        
        max_height = 0
        for i in range(m - 1):
            idx_left, height_left = restrictions[i]
            idx_right, height_right = restrictions[i + 1]
            
            idx_diff = idx_right - idx_left
            height_diff = abs(height_right - height_left)
            
            
            current_max = (height_left + height_right + idx_diff) // 2
            max_height = max(max_height, current_max)
            
        return max_height