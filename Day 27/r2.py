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
    merged=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    while i<len(left):
        merged.append(left[i])
        i+=1
    while j<len(right):
            merged.append(right[j])
            j+=1
    return merged
def binary(merged,target,l,r):
    if l>r:
        return "not found"
    mid=(l+r)//2
    if target==merged[mid]:
        return mid*mid
    elif target < merged[mid]:
        return binary(merged,target,l,mid-1)
    elif target> merged[mid]:
        return binary(merged,target,mid+1,r)
    else:
        return "Not found"
arr=[13,5,1,7,3,9,11]
sorted=split(arr)
l=0
r=len(sorted)-1
target=7
print(binary(sorted,target,l,r))
