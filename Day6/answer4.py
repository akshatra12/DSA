# Count Elements Greater Than 20
arr=[5,25,15,30,40,10]

count=0

for i in range(len(arr)):
    if arr[i]>20:
        count +=1

print(count)