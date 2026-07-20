#h1 
def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def binary(sorted,target,left,right):
    if left > right:
        return "not found"
    mid = (left + right) // 2
    if target == sorted[mid]:
        return fact(mid)
    elif target > sorted[mid]:
        return binary(sorted,target,mid+1,right)
    else:
        return binary(sorted,target,left,mid-1)

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)

arr = [8,3,6,1,9,2]
target = 6
sorted = insertion(arr)
left = 0
right = len(sorted) - 1
print(binary(sorted,target,left,right))