# R1
# observation: find the arget value and and we need to store all the visited middle elements in a dictonary and return that dictionary
# pattern: we apply binary search with hashing
# time complexity:O(log n)
# space complexity:O(log n)
# code:

def binary(arr,target,left,right,freq):
    if left>right:
        return "Not Found"
    mid =(left+right)//2
    new=arr[mid]
    if new in freq:
        freq[new]+=1
    else:
        freq[new]=1
    if target==new:
        return freq
    elif target>new:
        return binary(arr,target,mid+1,right,freq)
    else:
        return binary(arr,target,left,mid-1,freq)
arr = [2,4,6,8,10,12]
target = 10
left=0
right=len(arr)-1
freq={}
print(binary(arr,target,left,right,freq))
