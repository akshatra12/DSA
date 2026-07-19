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
    return best
    
def merge_sort(window):
    if len(window)<=1:
        return window
    mid=len(window)//2
    left=window[:mid]
    right=window[mid:]
    left_sorted=merge_sort(left)
    right_sorted=merge_sort(right)
    
    return merged(left_sorted,right_sorted)
def merged(left,right):
    i,j=0,0
    merge=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merge.append(left[i])
            i+=1
        else:
            merge.append(right[j])
            j+=1
    while i<len(left):
        merge.append(left[i])
        i+=1
    while j<len(right):
        merge.append(right[j])
        j+=1
    
    return merge
arr = [3,7,2,8,5,6,1]
k = 3
window=max_window(arr,k)
print(merge_sort(window))
