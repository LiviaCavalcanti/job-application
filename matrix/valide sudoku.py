"""
Determine if a 9 x 9 Sudoku board is valid.
Only filled cells are validated.
"""

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "5", ".", ".", ".", ".", "6", "."],
    ["5", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

def is_valid_sudoku(board):
    seen = set()

    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == ".":
                continue

            row_val = ('row', r, value)
            col_val= ('col', c, value)
            box_val = ('box', r // 3, c // 3, value)

            if row_val in seen or col_val in seen or box_val in seen:
                print(f"Duplicate found: {value} at row {r}, column {c}")
                return False
            seen.add(row_val)
            seen.add(col_val)
            seen.add(box_val)
    return True
    
print(is_valid_sudoku(board))
