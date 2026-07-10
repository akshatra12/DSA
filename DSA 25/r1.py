# #R1
# Observation:first i need to find max_sum and the  two sum

# Pattern:use sliding window and the  hashing for two sum

# Why this pattern?because we have a fixed window size and then we need to optimize the code

# Algorithm:
# 1.initialize a window sum
# 2. traverse the array from 0 to k(k is the size of window)
# 3.max_sum=window sum
# 4. again traverse the array from 1 to len(arr)+k-1
# 5. window sum= window sum - outgoing + incoming
# 6. check if max_sum is less then window sum then update the max_sum
# 7. repeat this until loop end
# 8.now target= max_sum
# 9.initialize a dictionary name-freq
# 10.again traverse the array with enumeration(index, num)
# 11. complement=target-num
# 12. check if complement in freq then return true
# 13. else update freq[num]=index
# 14.go to 10 until loop ends
# 15.if we don't find the target return False


# Time Complexity:O(n)

# Space Complexity:O(n)

# Code:
def two_sum(arr,k):
    win_sum=0
    for i in range(k):
        win_sum+=arr[i]
    target=win_sum
    for i in range(1,len(arr)-k+1):
        win_sum=win_sum-arr[i-1]+arr[i+k-1]
        if target<win_sum:
            target=win_sum
    freq={}
    for index,num in enumerate(arr):
        complement=target-num
        if complement in freq:
            return True
        else:
            freq[num]=index
    return False
arr = [3,1,4,1,5,9,2]
k = 3
print(two_sum(arr,k))

