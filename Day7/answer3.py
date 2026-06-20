# Most Frequent Number
arr = [5,5,5,1,1]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)
