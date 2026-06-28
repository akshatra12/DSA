#Range Sum (1 to 3)
def prefix_sum(arr):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    l=1
    r=3
    if l==0:
        sum=prefix[r]
    else:
        sum=prefix[r]-prefix[l-1]
        
    return sum
    
arr=[2,4,6,8,10]
print(prefix_sum(arr))