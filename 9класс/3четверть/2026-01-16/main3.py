

matrix1 = [[4,3,-4], [6,0,4]]
matrix2 = [[3, 2, 6, 3, 4], [-8, 5, 2, -6 ,3], [2, 7, 0, -2, 2]]

def matrixProducts(matrix1, matrix2):
    product = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                product[i][j] += matrix1[i][k] * matrix2[k][j]

    return product

print(matrix1)
print(matrix2)
print(matrixProducts(matrix1, matrix2))