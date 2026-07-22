# h1
def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
def binary(sorted,target,left,right):
    if left>right:
        return "Not found"
    mid=(left+right)//2
    if target==sorted[mid]:
        num=mid
        return power(num)
    elif target>sorted[mid]:
        return binary(sorted,target,mid+1,right)
    else:
        return binary(sorted,target,left,mid-1)
def power(num):
    if num==0:
        return 1
    else:
        return 2 ** num




arr = [12,5,8,1,15,10]
target = 10
sorted=insertion(arr)
left=0
right=len(sorted)-1
print(binary(sorted,target,left,right))