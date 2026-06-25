# Smallest Element
def smallest(arr):
    smallest_num=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<smallest_num:
            smallest_num=arr[i]
    return smallest_num
arr=[12,45,7,89,23]
print("The smallest number in the array is:", smallest(arr))