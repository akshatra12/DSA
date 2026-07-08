def search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if target==arr[mid]:
            return mid, arr[mid]
        elif target>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
arr = [10,20,30,40,50,60,70]
target = 50
print(search(arr,target))