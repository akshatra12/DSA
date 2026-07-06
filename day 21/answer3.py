#Merge Two Sorted Arrays
def merge(arr1,arr2):
    arr=[]
    i=0
    j=0
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
arr1 = [5,10,15]
arr2 = [1,2,20]
print(merge(arr1,arr2))