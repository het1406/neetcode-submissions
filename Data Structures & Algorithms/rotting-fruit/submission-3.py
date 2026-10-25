from collections import deque
from typing import List
class Solution: 
    def orangesRotting(self,grid):
        n = len(grid)
        m = len(grid[0])
        visited = set() 
        ans = 0 
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append(((i,j), 0))
                    visited.add((i,j))
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while q:
            (i,j),time = q.popleft()
            ans = max(ans,time)
            for dr, dc in directions:
                ni,nj = i+dr, j+dc
                if 0<=ni<n and 0<=nj<m and (ni,nj) not in visited and grid[ni][nj]==1:
                    q.append(((ni,nj),time+1))
                    visited.add((ni,nj))
                    grid[ni][nj]=2

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1 
        return ans