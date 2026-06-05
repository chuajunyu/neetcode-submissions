class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_nine(*args):
            """Takes in 9 strings, validate if there are no duplicate numbers"""
            numbers = [int(a) for a in args if a != "."]
            return len(numbers) == len(set(numbers))
        
        for row in board:
            if not is_valid_nine(*row):
                return False
        
        for c in range(9):
            col = [row[c] for row in board]
            if not is_valid_nine(*col):
                return False
            
        for x in range(3):
            start_row = x * 3
            for y in range(3):
                start_col = y * 3
                grid = []
                [grid.extend(row[start_col: start_col + 3]) for row in board[start_row:start_row + 3]]
                if not is_valid_nine(*grid):
                    return False
        
        return True