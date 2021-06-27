# Python program to convert a matrix to sparse matrix

# Display Normal Matrix
def displayMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")    # end=" " is used to place a space after displayed string
        print()

# Creating into a sparse matrix
def convertingTosparseMatrix(matrix):
    sparsematrix = []                 # created an empty list to store sparse sub rows
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                temp = []                # --- (1)

                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])

                # temp = [i, j, matrix[i][j]]  --- works same as (1)

                sparsematrix.append(temp)
    print("Sparse Matrix")
    displayMatrix(sparsematrix)


normalmatrix = [[1, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 4],
                [5, 0, 0, 0]]

displayMatrix(normalmatrix)
convertingTosparseMatrix(normalmatrix)