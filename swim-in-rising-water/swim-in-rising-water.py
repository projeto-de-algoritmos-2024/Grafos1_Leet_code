class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        top = max(2 * (n - 1), grid[0][0], grid[n - 1][n - 1])
        min_val = n * n - 1
        while top <= min_val:
            mid = (top + min_val) // 2
            visitados = set()
            if self.dfs(grid, visitados, 0, 0, mid):
                min_val = mid - 1
            else:
                top = mid + 1
        return top

    def dfs(self, grid, visitados, i, j, w_lvl):
        n = len(grid)
        if i < 0 or j < 0 or i >= n or j >= n or (i, j) in visitados or grid[i][j] > w_lvl:
            return False
        if i == n - 1 and j == n - 1:
            return True
        visitados.add((i, j))
        movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for movimento in movimentos:
            if self.dfs(grid, visitados, i + movimento[0], j + movimento[1], w_lvl):
                return True
        return False
