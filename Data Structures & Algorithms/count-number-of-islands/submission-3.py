class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0


        n = len(grid)  #number of rows 
        m = len(grid[0]) #number of coloumns 
        visited = set()
        islands_discovered = 0 

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:
                    self.dfs(i,j,grid,visited,n,m)
                    islands_discovered+=1
        return islands_discovered


    def dfs(self, i,j,grid,visited,n,m):
        if i<0 or j<0 or i>=n or j>=m or (i,j) in visited or grid[i][j]!='1':
            return 

        visited.add((i,j))
        self.dfs( i-1,j,grid,visited,n,m)
        self.dfs( i+1,j,grid,visited,n,m)
        self.dfs( i,j-1,grid,visited,n,m)
        self.dfs( i,j+1,grid,visited,n,m)


        
        