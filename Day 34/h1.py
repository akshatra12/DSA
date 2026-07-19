def binary(arr,target,left,right):
    if left>right:
        return -1
    mid=(left+right)//2
    if target==arr[mid]:
        return mid
    elif target>arr[mid]:
        return binary(arr,target,mid+1,right)
    else:
        return binary(arr,target,left,mid-1)

def pre(arr,left,right):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]= prefix[i-1]+arr[i]
    if left==0:
        prefix_sum=prefix[right]
    else:
        prefix_sum=prefix[right] - prefix[left-1]
    return prefix_sum
arr = [2,4,6,8,10,12,14]
target = 10
left=0
r=len(arr)-1
right=binary(arr,target,left,r)
if right==-1:
    print("target not found")
else:
    print(right , pre(arr,left,right))

