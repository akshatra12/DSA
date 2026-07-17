# R2
def checkUniqueWindow(arr,k):
    win_sum=0
    window=[]
    for i in range(k):
        win_sum+=arr[i]
        window.append(arr[i])
    best=window
    max_sum=win_sum
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
            freq[i]+=1
        else:
            freq[i]=1
    for key,value in freq.items():
        if value!=1:
            return False
    return True
    
arr = [2,5,2,7,7,8,9]
k = 3
print(checkUniqueWindow(arr,k))