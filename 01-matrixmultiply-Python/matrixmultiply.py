# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    m1_row = len(m1)
    m1_col = len(m1[0])
    m2_row = len(m2)
    m2_col = len(m2[0])
    if m1_col != m2_row:
        return None
    mat_mul = [[0 for x in range (m2_col)] for y in range(m1_row)]
    for i in range(m1_row):
        for j in range(m2_col):
            for k in range(m2_row):
                mat_mul[i][j] += m1[i][k] * m2[k][j]

    return mat_mul




