
def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col],end=" ")
        print()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print_matrix(matrix)
