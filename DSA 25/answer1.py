# #1,2,3,4
# Observation: i have two sorted array and we need to merge them in a single sorted array

# Pattern: two pointers

# Why this pattern? because we need to traverse two array at the same time and two pointers do this in single loop

# Algorithm:

# Time Complexity:O(n)

# Space Complexity:O(n)

# Code:
  #1
def merge(arr1,arr2):
    i,j=0,0
    arr=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
    return arr
arr1 = [1,4,7]
