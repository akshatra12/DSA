def non_repeat(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for key,value in freq.items():
          if value==1:
              return key
arr = [4,5,4,5,4,6,7]
print(non_repeat(arr))