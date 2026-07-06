#Q5 Unique Elements
def unique(arr):
    seen=set()
    for i in arr:
        if i not in seen:
            seen.add(i)
            
    return seen
arr = [1,1,2,2,3,4,4,5]
print(unique(arr))