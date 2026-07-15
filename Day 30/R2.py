# R2
# Observation:first we need to sort the array and then we find the target from that sorted array
# pattern:merge sort+ binary search
# time complexity:O(nlogn)
# space complexity:O(nlogn)
def split(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left_sorted=split(left)
    right_sorted=split(right)
    
    return merge(left_sorted,right_sorted)
def merge(left,right):
    i,j=0,0
    sorted=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    while i<len(left):
        sorted.append(left[i])
        i+=1
    while j<len(right):
        sorted.append(right[j])
        j+=1
    return sorted
def binary(sorted,target,left,right):
    if left>right:
        return "Not found"
    mid=(left+right)//2
    if target==sorted[mid]:
        return mid,sorted[mid]
    elif target>sorted[mid]:
        return binary(sorted,target,mid+1,right)
    else:
        return binary(sorted,target,left,mid-1)
arr = [14,3,9,7,21,18,5]
target = 18
sorted=split(arr)
left=0
right=len(sorted)-1
print(binary(sorted,target,left,right))
