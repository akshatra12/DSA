#Binary Search
def binary(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if target==arr[mid]:
            return mid
        elif target>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[10,20,30,40,50,60,70,80,90]
target=80
print(binary(arr,target))

