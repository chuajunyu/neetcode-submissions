class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_nine(*args): # O(n)
            """Takes in 9 strings, validate if there are no duplicate numbers"""
            numbers = [int(a) for a in args if a != "."]
            return len(numbers) == len(set(numbers))
        
        for row in board: # O(n)
            if not is_valid_nine(*row):
                return False
        
        for c in range(9): # O(n)
            col = [row[c] for row in board] # O(n)
            if not is_valid_nine(*col): # O(n)
                return False
            
        for x in range(3):
            start_row = x * 3
            for y in range(3):
                start_col = y * 3
                grid = []
                for p in range(start_row, start_row + 3):
                    for q in range(start_col, start_col + 3):
                        grid.append(board[p][q])
                if not is_valid_nine(*grid):
                    return False
        
        return True