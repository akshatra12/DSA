#R1
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
    
def binary(sorted,target,left,right):
    if left>right:
        return -1
    mid=(left+right)//2
    
    if target==sorted[mid]:
        return mid
    elif target>sorted[mid]:
        return binary(sorted,target,mid+1,right)
    else:
        return binary(sorted , target , left , mid-1)
arr = [14,3,8,1,20,7]
target = 8
sorted=split(arr)
left=0
right=len(sorted)-1
print(binary(sorted,target,left,right))