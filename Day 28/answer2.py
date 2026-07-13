# 2

# Observation:we need to find the target and also then find the first unique element

# Pattern:we use merge sort and then apply and then find the first unique element with the help of hashing

# Why this pattern?because the complexity of merge sort is good in compare to other sorting techniques we learned and then simple we find the unique element with the help of hashing

# Time Complexity:O(n)

# Space Complexity: O(n) 

# code:
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
    while j < len(right):
        merged.append(right[j])
        j+=1
    return merged
def check_unique(sorted):
    freq={}
    for i in sorted:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for key in freq:
        if freq[key]==1:
            return key
    return "no unique element"
arr = [5,2,4,2,1,5,7]
sorted=split(arr)
print(check_unique(sorted))
