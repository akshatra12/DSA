def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def binary(arr,target,left,right):
    if left>right:
        return "Not Found"
    mid=(left+right)//2
    if target==arr[mid]:
        index=mid
        return fact(index)
    elif target>arr[mid]:
        return binary(arr,target,mid+1,right)
    else:
        return binary(arr,target,left,mid-1)
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
arr = [11,4,8,2,15,6]
target = 8
sorted=bubble(arr)
left=0
right=len(sorted)-1
print(binary(sorted,target,left,right))