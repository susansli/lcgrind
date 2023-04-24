# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according
# to the following rules:
# 1) Each row must contain the digits 1-9 without repetition.
# 2) Each column must contain the digits 1-9 without repetition.
# 3) Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules (there's no need to solve
# for the missing cells first)

# There's really only one way to solve this and that's to check every row, column, and square block.
# To do so I made dictionaries of sets for O(1) access time. That being said, I do still need to iterate
# through every individual cell and potentially store it, giving the solution a O(N^2) time and space complexity.

def is_valid_sudoku(board):
    row_validation = set()
    square_validation = {i: set() for i in range(1, 10)}
    column_validation = {i: set() for i in range(1, 10)}
    square_row_counter = 0  # this counts what "row" each 3x3 block is on

    for i in range(len(board)):
        row_validation.clear()
        column_counter = 1
        square_number = 1 + (square_row_counter * 3)

        for j in range(len(board[i])):
            if board[i][j] != ".":
                if board[i][j] in row_validation or board[i][j] in square_validation[square_number] or \
                        board[i][j] in column_validation[column_counter]:
                    return False

                row_validation.add(board[i][j])
                square_validation[square_number].add(board[i][j])
                column_validation[column_counter].add(board[i][j])

            column_counter += 1

            if (j + 1) % 3 == 0:
                square_number += 1

        if (i + 1) % 3 == 0:
            square_row_counter += 1

    return True

