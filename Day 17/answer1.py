# Binary Search
def binary(arr,target):
     left=0
     right=len(arr)-1 
     while left<=right: 
         mid = (left+right)//2 
         if target==arr[mid]: 
             return mid 
         elif target<arr[mid]: 
             right=mid-1 
         else: 
             left=mid+1 
     return -1 
arr=[10,20,30,40,50,60,70] 
target=40 
print(binary(arr,target))