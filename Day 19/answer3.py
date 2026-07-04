#Q3: Count Swaps
def selection(arr):
    n=len(arr)
    count=0
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        count+=1
    return count
arr=[5,2,4,1,3]
print(selection(arr))
