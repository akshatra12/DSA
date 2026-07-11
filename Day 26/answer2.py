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
arr = [2,5,67,8,91,35,4,6,7,8,9,10] 
print(split(arr))