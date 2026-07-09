def count_even(matrix):
    count=0
    for row in matrix:
        for value in row:
            if value%2==0:
                 count+=1
    return count
matrix = [
    [2,5,8],
    [1,6,9]
]
print(count_even(matrix))