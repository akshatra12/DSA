# Search 100
found = False
arr=[5,10,15,20]
target=100

for i in arr:
    if i == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")