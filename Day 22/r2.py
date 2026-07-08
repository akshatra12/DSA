# R2 Sliding Window + Prefix Sum
def pre_sl(arr,k,left,right):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    win_sum=0
    pre_sum=0
    for i in range(k):
        win_sum+=arr[i]
 
    maximum=win_sum
 
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    for i in range(len(arr)-k+1):
        win_sum=win_sum-arr[i-1]+arr[i+k-1]
    print(win_sum)
    print(prefix)
    if left==0:
        pre_sum=prefix[right]
    else:
        pre_sum=prefix[right]-prefix[left-1]
    return pre_sum
arr = [2,1,5,1,3,2,6]
k=3
left=2
right=5
print(pre_sl(arr,k,left,right))