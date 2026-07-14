# R2
# Observation: we need to find the window whose sum is maximum and then find the sum of range 2 to 5 and the  return both values
# pattern:sliding maximum sum window and prefix sum
# time complexity:O(n)
# space complexity:O(k+n)
# code:
def range_sum(arr,k,left,right):
    win_sum=0
    window=[]
    for i in range(k):
        win_sum+=arr[i]
        window.append(arr[i])
    max_sum=win_sum
    best_window=window
    for i in range(1,len(arr)-k+1):
        win_sum=win_sum-arr[i-1]+arr[i+k-1]
        window.remove(arr[i-1])
        window.append(arr[i+k-1])
        if max_sum<win_sum:
            max_sum=win_sum
            best_window=window.copy()
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    if left==0:
        prefix_sum=prefix[right]
    else:
        prefix_sum=prefix[right] - prefix[left-1]
    return best_window,prefix_sum
arr = [3,1,2,6,4,5]
k = 3
left=2
right=5
print(range_sum(arr,k,left,right))
