def element_sum(matrix):
    sum=0
    for row in matrix:
        for value in row:
            sum+=value
    return sum
matrix = [
    [1,2,3],
    [4,5,6]
]
print(element_sum(matrix))