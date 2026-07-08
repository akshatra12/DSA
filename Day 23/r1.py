# R1: Sliding Window + Binary Search
def search(arr,k,sorted_arr):
    win_sum=0
    for i in range(k):
        win_sum+=arr[i]
    max_sum=win_sum
    for i in range(1,len(arr)-k+1):
        win_sum=win_sum-arr[i-1]+arr[i+k-1]
        if max_sum<win_sum:
            max_sum=win_sum
    print(max_sum)
    target=max_sum
    left=0
    right=len(sorted_arr)-1
    while left<=right:
        mid=(left+right)//2
        if target==sorted_arr[mid]:
              return mid
        elif target>sorted_arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
arr = [2,5,1,8,2,9,1]
k = 3
sorted_arr = [6,8,10,12,14,16,18,20]
print(search(arr,k,sorted_arr))