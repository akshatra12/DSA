# R2 (Binary Search + Two Pointers)
def search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if target==arr[mid]:
            return "found"
        elif target>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    else:
        left=0
        right=len(arr)-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    return arr
arr = [10,20,30,40,50,60,70]
target = 90
print(search(arr,target))
