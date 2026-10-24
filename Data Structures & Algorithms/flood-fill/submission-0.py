class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        visited = set() 
        original_color = image[sr][sc]
        n = len(image)
        m = len(image[0])
        self.dfs(sr, sc, image, visited,n,m, original_color,color)
        return image 

    def dfs(self, i, j, image, visited,n,m, original_color,color):
        if i<0 or j<0 or i>=n or j>=m or (i,j) in visited or image[i][j]!= original_color:
            return 

        visited.add((i,j))
        image[i][j] = color
        self.dfs(i-1, j, image, visited, n, m, original_color, color)
        self.dfs(i+1, j, image, visited, n, m, original_color, color)
        self.dfs(i, j-1, image, visited, n, m, original_color, color)
        self.dfs(i, j+1, image, visited, n, m, original_color, color)

            
        