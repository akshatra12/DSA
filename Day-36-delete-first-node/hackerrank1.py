# h1
# Time complexity : O(n^2)
def selection(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
def binary(sorted,target,left,right):
    if left>right:
        return"Not Found"
    mid=(left+right)//2
    if target==sorted[mid]:
        r_index=mid
        return r_index
    elif target > sorted[mid]:
        return binary(sorted,target,mid+1,right)
    else:
        return binary(sorted,target,left,mid-1)
def pre_sum(sortedl,l,r):
    prefix=[0]*len(sorted)
    prefix[0]=sorted[0]
    for i in range(1,len(sorted)):
        prefix[i]=prefix[i-1]+sorted[i]
    if l==0:
        prefix_sum=prefix[r]
    else:
        prefix_sum=prefix[r]-prefix[l-1]
    return prefix_sum
arr = [9,3,7,1,8,2]
target = 7
sorted=selection(arr)
left=0
right=len(sorted)-1
r=binary(sorted,target,left,right)
print(pre_sum(sorted,left,r))
