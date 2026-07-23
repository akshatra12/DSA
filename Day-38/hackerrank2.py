def MaxSumWindow(arr,k):
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
    return CheckPalindrome(best)

def CheckPalindrome(best):
    left=0
    right=len(best)-1
    while left<right:
        if best[left]!=best[right]:
            
            return "Not Palindrome"
        left+=1
        right-=1
    freq={}
    for i in best:
        if i in freq:
            return i
        else:
            freq[i]=1
    return "No duplicate"
arr = [3,7,3,8,5,5,8]
k = 4
print(MaxSumWindow(arr,k))

