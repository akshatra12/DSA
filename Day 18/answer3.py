# Q3 Count Swaps

def bubble(arr):
    count=0
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
             if arr[j]>arr[j+1]:
                 count+=1
                 arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return count
arr=[5,2,4,1,3]
print(bubble(arr))