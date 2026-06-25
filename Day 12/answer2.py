#Largest Element
def largest(arr):
    largest_num=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest_num:
            largest_num=arr[i]
    return largest_num
arr=[12,45,7,89,23]
print("The largest number in the array is:", largest(arr))



