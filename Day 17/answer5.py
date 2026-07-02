#Implement Binary Search recursively
def binary(arr,target,left,right):
     if left<=right: 
         mid = (left+right)//2 
         if target==arr[mid]: 
             return mid 
         elif target<arr[mid]: 
             return binary(arr,target,left,mid-1) 
         else: 
             return binary(arr,target,mid+1,right) 
     else: 
         return -1 
arr=[10,20,30,40,50,60,70] 
target=70 
left=0 
right=len(arr)-1 
print(binary(arr,target,left,right))