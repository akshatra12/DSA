# Q1 Bubble Sort
# arr=[5,2,4,1,3]


def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
             if arr[j]>arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr
arr=[5,2,4,1,3]
print(bubble(arr))