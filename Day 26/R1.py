#R1
# Observation:first we need to find maximum sum of window size k and also build a -prefix sum array then check max sum is equal to any element of prefix sum 
# # Pattern:we apply sliding window to find the sum and then we apply prefix sum and then we compare both to check the last condition 
# # Algorithm: 
# # 1.create a function (range_sum) and pass arguments(arr,k) 
# # 2.initialize window sum=0 
# # 3.start a loop of range k 
# # 4.window sum+=arr[i] 
# # 5.repeat untill loop break 
# # 6.max_sum=window sum 
# # 7.again start a loop of range 1 to len(arr)-k+1 
# # 8.window sum = window sum -outgoing + incoming 
# # 9. check max_sum<window sum if yes then update the value of max_sum 
# # 10.repeat untill loop break 
# # 11.initialize a array for prefix sum name-prefix[] 
# # 12. prefix[0]=arr[0] # 13. again start a loop from 1 to len(arr) 
# # 14.prefix[i]=prefix[i-1]+arr[i] 
# # 15 check if max_sum in prefix then return True 
# # 16.repeat untill it break 
# # 17.if max_sum not in prefix then return False 
# # Time Complexity:O(n) 
# # Space Complexity:O(n) 
# # Code 
def range_sum(arr,k): 
    win_sum=0 
    for i in range(k): 
        win_sum+=arr[i] 
    max_sum=win_sum 
    for i in range (1,len(arr)-k+1): 
        win_sum=win_sum-arr[i-1]+arr[i+k-1] 
        if max_sum<win_sum: 
            max_sum=win_sum 
    prefix=[0]*len(arr) 
    prefix[0]=arr[0] 
    for i in range(1,len(arr)): 
        prefix[i]=prefix[i-1]+arr[i] 
    left=0
    right=len(prefix)-1
    while left<=right:
        if left==0:
            range_sum=prefix[right]
            left+=1
            if range_sum==max_sum:
                return True
        else:
            range_sum=prefix[right]-prefix[left-1]
            left+=1
            if range_sum==max_sum:
                return True
     
        right-=1
    return False
    return False 
arr = [2,4,6,8,10,12] 
k = 3 
print(range_sum(arr,k))