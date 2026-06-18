# Linear Search (25 Found)
found = False
arr=[10,15,20,25,30]
target=25

for i in arr:
    if i == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")