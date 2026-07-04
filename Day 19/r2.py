#Sliding Window
def max_sum(arr,k):
    win_sum=0
    for i in range(k):
        win_sum+=arr[i]
    maximum=win_sum
    for i in range(1,len(arr)-k+1):
        win_sum=win_sum-arr[i-1]+arr[i+k-1]
        if maximum<win_sum:
            maximum=win_sum
    return maximum
arr=[4,2,1,7,8,1,2,8]
k=3
print(max_sum(arr,k))
