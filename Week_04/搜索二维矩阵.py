class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix==[] or matrix == [[]]:
            return False
        l,r = len(matrix),len(matrix[0])
        start,end = 0,l*r-1
        while start <= end:
            mid = (end-start)//2 + start
            if matrix[mid//r][mid%r] == target:
                return True
            elif matrix[mid//r][mid%r] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False