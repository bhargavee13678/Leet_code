class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows,cols= len(matrix),len(matrix[0])
        top, bot= 0,rows-1
        while top<= bot:
            mid= (top+bot)//2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bot= mid-1
            else:
                break 
        if not (top<= bot):
            return False
        
        mid= (top+bot)//2
        l,r= 0,cols-1
        while l<=r:
            middle= (l+r)//2
            if target < matrix[mid][middle]:
                r= middle-1
            elif target > matrix[mid][middle]:
                l= middle +1
            else:
                return True
        return False
        