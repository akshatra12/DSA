#3
# Observation:first we need to find the index of the target value and then we  need to find prefix sum from index 0 to the index 

# Pattern: binary search and prefix sum

# Why this pattern?for findig the index we use binary search and for find the prefix sum from 0 to index we use prefix sum

# Time Complexity:O(log n + n)

# Space Complexity:O(n)
# code:
def binary(arr,target,left,right):
    if left>right:
        return "not found"
    mid=(left+right)//2
    if target==arr[mid]:
        return mid
    elif target<arr[mid]:
        return binary(arr,target,left,mid-1)
    else:
        return binary(arr,target,mid+1,right)
def prefix_sum(arr,l,index):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    if l==0:
        pre_sum=prefix[index]
    else:
        pre_sum=prefix[index]-prefix[l-1]
    return pre_sum
arr = [2,4,6,8,10,12]
target = 8
left=0
right=len(arr)-1
r=binary(arr,target,left,right)
print(prefix_sum(arr,l=0,index=r))