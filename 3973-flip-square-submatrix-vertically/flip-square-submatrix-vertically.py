class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
      
        for i in range(k//2):
            for j in range(k):
                grid[x+i][y+j], grid[x+(k-1-i)][y+j] = grid[x+(k-1-i)][y+j], grid[x+i][y+j]
        return grid