# brute force
def two_sum(arr,target):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                print(i,j)
                count+=1
    return count
arr = [1,5,7,-1,5]
target = 6
print(two_sum(arr,target))

# time complexity = O(n^2)
# space complexity=O(1)
