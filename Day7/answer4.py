# Duplicate Detection
arr = [1,2,3,4,2]
freq={}

for num in arr:
    if num in freq:
        freq[num]+=1
        print("duplicate found")
        break
    else:
        freq[num]=1