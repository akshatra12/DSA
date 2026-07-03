# Q2 Bubble Sort
# arr=[10,7,8,9,1,5]

def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
             if arr[j]>arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr
arr=[10,7,8,9,1,5]
print(bubble(arr))