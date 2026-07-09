
#R1
def check_duplicate(arr,k):
    win_sum=0
    window=[]
    for i in range(k):
        win_sum+=arr[i]
        window.append(arr[i])
    best_window=window
    max_sum=win_sum
    for i in range(1,len(arr)-k+1):
        win_sum=win_sum-arr[i-1]+arr[i+k-1]
        window.remove(arr[i-1])
        window.append(arr[i+k-1])
        if max_sum<win_sum:
             max_sum=win_sum
             best_window=window.copy()
    freq={}
    for i  in best_window:
        if i in freq:
            return True
        else:
            freq[i]=1
    return False
arr = [1,2,3,2,5,2,1]
k = 4
print(check_duplicate(arr,k))