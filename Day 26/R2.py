#R2
def check_duplicate(matrix):
    freq = {}
    for row in matrix:
        for col in row:
            if col in freq:
                return True
            else:
                freq[col] = 1
    return False
matrix = [
    [1,2,2],
    [3,4,4],
    [5,6,7]
]
print(check_duplicate(matrix))