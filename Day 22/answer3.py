# Q3 First Duplicate
def hash(arr):
    seen=set()
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            return i
arr=[3,1,4,2,5,4,6]
print(hash(arr))