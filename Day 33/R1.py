# R1
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    
    left_sorted=merge_sort(left)
    right_sorted=merge_sort(right)
    
    return merged(left_sorted,right_sorted)

def merged(left,right):
    i,j=0,0
    merge=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merge.append(left[i])
            i+=1
        else:
            merge.append(right[j])
            j+=1
    while i < len(left):
        merge.append(left[i])
        i+=1
    while j<len(right):
        merge.append(right[j])
        j+=1
    return merge
def binary(sorted,target,left,right):
    if left>right:
        return "Not found"
    mid=(left+right)//2
    if target==sorted[mid]:
        return mid
    elif target>sorted[mid]:
        return binary(sorted,target,mid+1,right)
    else:
        return binary(sorted,target,left,mid-1)
        
arr = [9,2,7,4,1,6]
target = 7
sorted=merge_sort(arr)
left=0
right=len(sorted)-1
print(binary(sorted,target,left,right))
