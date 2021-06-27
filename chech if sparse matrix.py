matrix = [
    [ 5, 5, 9, 0, 0 ],
    [ 5, 0, 3, 0, 0 ],
    [ 5, 7, 2, 0, 0 ],
    [ 9, 7, 2, 0, 0 ],
    [ 0, 3, 2, 0, 0 ]
]

zeros = 0

for row in matrix:
    for e in row:
        if e == 0:
            zeros += 1

totalElems = len(matrix) * len(matrix[0])

if zeros > totalElems:
    print("Matrix is sparse!")
else:
    print("Matrix is dense!")