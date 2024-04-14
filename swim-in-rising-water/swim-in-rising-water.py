class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        visitados = set()

    def visitar_quadrado(grid, visitados, i, j, lvl = 0):
        if 0 <= i < n or 0 <= j < n or (i,j) not in visitados:
            if(i == n-1 and j == n-1): return max(lvl,grid[i][j])
            visitados.add((i,j))
            lvl = max(lvl,grid[i][j])
            return min(visitar_quadrado(grid,visitados,i+1,j,lvl),visitar_quadrado(grid,visitados,i,j+1,lvl),visitar_quadrado(grid,visitados,i-1,j,lvl),visitar_quadrado(grid,visitados,i,j-1,lvl))
        