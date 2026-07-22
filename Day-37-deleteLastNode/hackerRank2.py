def max_window(arr,k):
    win_sum=0
    window=[]
    for i in range(k):
        win_sum+=arr[i]
        window.append(arr[i])
    max_sum=win_sum
    best=window
    
    for i in range(1,len(arr)-k+1):
        win_sum=win_sum-arr[i-1]+arr[i+k-1]
        window.remove(arr[i-1])
        window.append(arr[i+k-1])
        if max_sum<win_sum:
             max_sum=win_sum
             best=window.copy()
    freq={}
    for i in best:
        if i in freq:
            return f"Duplicate found"
        else:
            freq[i]=1
    return "duplicate not found"
def prefix_sum(arr,left,right):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    if left==0:
        return prefix[right]
    else:
        return prefix[right]-prefix[left-1]
arr = [4,2,7,3,6,1,8,5]
k = 3
left = 2
right = 6
print(max_window(arr,k))
print(prefix_sum(arr,left,right))
