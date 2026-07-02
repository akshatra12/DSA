# Count how many iterations Binary Search takes to find:

#target= 60

# inside:

# [10,20,30,40,50,60,70]
def binary(arr,target):
     left=0
     right=len(arr)-1
     count=0
     while left<=right:
         count += 1
         mid = (left+right)//2
         if target==arr[mid]:
             return count
         elif target<arr[mid]:
             right=mid-1
         else:
             left=mid+1
     return count
arr=[10,20,30,40,50]
target=15
print(binary(arr,target))