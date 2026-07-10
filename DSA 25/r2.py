# #R2
# Observation: i need to find the index of the target value and then find the factorial of that index

# Pattern: for finding the index of the target we apply binary search using recursion and then we again use recursion for find the factorial

# Why this pattern? Because recursion reduce the line of codes and also optimize the code

# Algorithm:
# 1.we have a array and a target value
# 2. initialize left =0 and right= length of arr -1
# 3.make a function and pass all the values like arr , target, left and right
# 4.find the mid value mid=(left+right)//2
# 5.now check if target == arr[mid] then return mid
# 6.if target > arr[mid] then again call the function and pass (arr, target,mid+1,right)
# 7.if target < arr[mid] then again call the function and pass (arr,target,left,mid-1)
# 8. else return -1
# 9.index = function1( arr , target, left, right)
# 10.again create a function for the factorial
# 11. check if index==0 or 1 then return 1
# 12. else again recursively call the function index*function2(index-1)

# Time Complexity:O(log n + index)

# Space Complexity:O(log n + index)

# Code:

def binary(arr,target,left,right):
    if left>right:
        return "Not Found"
    mid=(left+right)//2
    if target==arr[mid]:
        return mid
    elif target>arr[mid]:
        return binary(arr,target,mid+1,right)
    elif target<arr[mid]:
        return binary(arr,target,left,mid-1)
    else:
        return -1
arr = [5,10,15,20,25,30,35]
target = 20
left=0
right=len(arr)-1
index=binary(arr,target,left,right)

if index==-1:
    print("not found")
else:
     def fact(index):
          if index==0 or index==1:
              return 1
          else:
              return index*fact(index-1)
     print(fact(index))
