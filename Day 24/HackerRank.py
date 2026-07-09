def sum_ind(arr,target):
    freq={}
    complement=0
    for index , num in enumerate(arr):
        complement=target-num
        if complement in freq:
            return freq[complement],index
        else:
            freq[num]=index
    return -1
arr=[2,11,15,7]
target=9
print(sum_ind(arr,target))
