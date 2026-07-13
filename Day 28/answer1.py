# 1
# Observation:find the window of the maximum sum and then find the duplicate element of that window

# Pattern: for finding the window sum we use sliding window concept and for finding the dplicate we use hashing

# Why this pattern?we use sliding window because we have a fixed size window and for find the duplicate we use a dictinory to find it

# Time Complexity:O(n)

# Space Complexity:0(n)

# code:

def check_duplicate(arr,k):
    win_sum=0
    window=[]
    for i in range(k):
        win_sum+=arr[i]
        window.append(arr[i])
    max_sum=win_sum
    best_window=window
    print(window)
    print(max_sum)
    for i in range(1,len(arr)-k+1):
        win_sum=win_sum-arr[i-1]+arr[i+k-1]
        window.remove(arr[i-1])
        window.append(arr[i+k-1])
        print(window)
        print(win_sum)
        if  max_sum<win_sum:
            max_sum=win_sum
            print(max_sum)
            best_window=window
            print(best_window)
    print(max_sum)
    print(best_window)
    freq={}
    for i in best_window:
        if i in freq:
            return True
        else:
            freq[i]=1
    return False
arr = [1,2,2,3,4,5,2]
k = 4
print(check_duplicate(arr,k))

