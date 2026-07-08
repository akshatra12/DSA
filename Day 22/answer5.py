
def unique(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq.keys()
arr = [1,2,2,3,1,4,5,5]
result=unique(arr)
print(result)