#Revision 1: Binary Search
def binary(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if target==arr[mid]:
              return mid
        elif target>arr[mid]:
              left=mid+1
        elif target<arr[mid]:
              right=mid-1
        else:
              return -1
    

arr=[10,20,30,40,50,60,70]
target=50
print(binary(arr,target))
