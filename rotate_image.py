# solve this recursively -
# if the length of the row - 2 <= 1, then return
# otherwise, starting clockwise, change rows to columns and columns into rows

def rotate_matrix(matrix: list[list[int]], current_iteration=0):
    if len(matrix) - (current_iteration * 2) <= 1:
        return
    matrix_length = len(matrix) - current_iteration - 1

    for i in range(len(matrix) - (current_iteration * 2) - 1):
        # TOP ROW --> RIGHT COL
        temp_1 = matrix[i + current_iteration][matrix_length]  # save right col value
        # right col = top row
        matrix[i + current_iteration][matrix_length] = matrix[current_iteration][i + current_iteration]
        if current_iteration == 2:
            print(temp_1)

        # RIGHT COL --> BOTTOM ROW
        temp_2 = matrix[matrix_length][matrix_length - i]  # save bottom row value
        # bottom row = right col
        if current_iteration == 2:
            print(temp_2)
        matrix[matrix_length][matrix_length - i] = temp_1
        if current_iteration == 2:
            print(matrix[matrix_length][matrix_length - i])

        # BOTTOM ROW --> LEFT COL
        temp_1 = matrix[matrix_length - i][current_iteration]  # save left col value
        # left col = bottom row
        matrix[matrix_length - i][current_iteration] = temp_2

        # LEFT COL --> TOP ROW
        matrix[current_iteration][i + current_iteration] = temp_1

    current_iteration += 1

    rotate_matrix(matrix, current_iteration)


if __name__ == '__main__':
    test_matrix = [[2, 29, 20, 26, 16, 28], [12, 27, 9, 25, 13, 21], [32, 33, 32, 2, 28, 14], [13, 14, 32, 27, 22, 26],
                   [33, 1, 20, 7, 21, 7], [4, 24, 1, 6, 32, 34]]
    print("MATRIX 1 BEFORE:")
    for j in range(len(test_matrix)):
        print(test_matrix[j])

    rotate_matrix(test_matrix)

    print("\nMATRIX 1 AFTER:")
    for j in range(len(test_matrix)):
        print(test_matrix[j])

    print()
    expected = [[4, 33, 13, 32, 12, 2], [24, 1, 14, 33, 27, 29], [1, 20, 32, 32, 9, 20], [6, 7, 27, 2, 25, 26],
                [32, 21, 22, 28, 13, 16], [34, 7, 26, 14, 21, 28]]
    for j in range(len(expected)):
        print(expected[j])
