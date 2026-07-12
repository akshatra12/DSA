# R1
def first_unique(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for key in freq:
        if freq[key]==1:
            return key
     
arr = [1,2,1,2,5]
print(first_unique(arr))
