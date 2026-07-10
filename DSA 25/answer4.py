# 4
def merge(arr1,arr2):
    i,j=0,0
    arr=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
    return arr
arr1 = [1,3,5]
arr2 = []
print(merge(arr1,arr2))

