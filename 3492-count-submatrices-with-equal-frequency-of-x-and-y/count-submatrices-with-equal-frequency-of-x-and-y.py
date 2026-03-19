class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        x_count = [[0] * (n + 1) for _ in range(m + 1)]
        y_count = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0

        for i in range(m):
            for j in range(n):
                x_count[i + 1][j + 1] = (
                    (1 if grid[i][j] == 'X' else 0) +
                    x_count[i][j + 1] +
                    x_count[i + 1][j] -
                    x_count[i][j]
                )
                y_count[i + 1][j + 1] = (
                    (1 if grid[i][j] == 'Y' else 0) +
                    y_count[i][j + 1] +
                    y_count[i + 1][j] -
                    y_count[i][j]
                )
                

                if x_count[i + 1][j + 1] > 0 and x_count[i + 1][j + 1] == y_count[i + 1][j + 1]:
                    ans += 1
                    
        return ans