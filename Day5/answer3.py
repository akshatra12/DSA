#Count Occurrences
arr=[5,2,5,8,5,10]
target=5

count = 0

for i in arr:
    if i==target:
        count +=1

print(count)