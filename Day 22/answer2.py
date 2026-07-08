# Q2 Count Unique
def hash(arr):
    seen=set()
    count=0
    for i in arr:
        if i not in seen:
            seen.add(i)
            count+=1
    return count
arr=[1,2,2,3,4,4,5]
print(hash(arr))