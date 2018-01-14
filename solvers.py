

def find_determinant_2x2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]


def find_determinant_3x3(matrix):
    a, b, c = matrix[0]
    c1 = a * find_determinant_2x2(matrix[1:3, [1, 2]])
    c2 = b * find_determinant_2x2(matrix[1:3, [0, 2]])
    c3 = c * find_determinant_2x2(matrix[1:3, [0, 1]])
    return c1 - c2 + c3


def find_determinant_4x4(matrix):
    a, b, c, d = matrix[0]
    c1 = a * find_determinant_3x3(matrix[1:4, [1, 2, 3]])
    c2 = b * find_determinant_3x3(matrix[1:4, [0, 2, 3]])
    c3 = c * find_determinant_3x3(matrix[1:4, [0, 1, 3]])
    c4 = c * find_determinant_3x3(matrix[1:4, [0, 1, 2]])
    return c1 - (c2 + c3 + c4)


DETERMINANT_SOLVERS = {
    2: find_determinant_2x2,
    3: find_determinant_3x3,
    4: find_determinant_4x4,
}
