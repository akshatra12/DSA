# Count how many comparisons your merge algorithm performs for:
def merge(arr1,arr2):
    arr=[]
    i=0
    j=0
    count=0
    while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr.append(arr1[i])
                i+=1
                count+=1

            else:
                arr.append(arr2[j])
                j+=1
                count+=1
    while i<len(arr1):
         arr.append(arr1[i])
         count+=1
         i+=1
    while j<len(arr2):
         arr.append(arr2[j])
         count+=1
         j+=1
    return count
arr1 = [1,3,5]
arr2 = [2,4,6]
print(merge(arr1,arr2))