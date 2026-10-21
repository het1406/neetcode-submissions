class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0])-1
        len1 = len(matrix[0])
        
        while l<=r:
            mid = (l+r)//2
            row = mid//len1
            col = mid%len1
            x= matrix[row][col]
            if target < x:
                r = mid - 1
            elif target > x:
                l = mid + 1
            else:
                return True 
        return False

        