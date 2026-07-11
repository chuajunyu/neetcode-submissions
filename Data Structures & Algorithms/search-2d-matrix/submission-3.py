class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Build a function to lookup indexes in the matrix
        # then just run regular binary search
        
        m = len(matrix)
        n = len(matrix[0])

        def lookup_matrix(index):
            if index < 0 or index >= m * n:
                # Out of Range
                raise Exception("Out of range")

            row = index // n
            column = index % n
            return matrix[row][column]

        left, right = 0, m * n - 1
        while left <= right and left < m * n and right >= 0:
            middle = (left + right) // 2

            value = lookup_matrix(middle)

            if value == target:
                return True
            elif value < target:
                left = middle + 1
            else:
                right = middle - 1

        return False        