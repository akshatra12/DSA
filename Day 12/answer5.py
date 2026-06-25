#Second largest
def Second_largest(arr):
    first =second = 0
    for i in arr:
        if i >first:
            second = first
            first=i
        elif i>second and i<first:
            second=i
    return second
arr=[10,20,5,40,30]
print(Second_largest(arr))