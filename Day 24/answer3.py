def find_largest(matrix):
    largest=matrix[0][0]
    for row in matrix:
        for value in row:
            if largest<value:
                largest=value
    return largest
matrix = [
    [3,8,2],
    [9,1,7]
]
print(find_largest(matrix))