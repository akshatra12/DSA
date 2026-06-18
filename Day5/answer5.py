# Second Largest
arr=[12,45,7,89,23]

max=arr[0]
second_max=arr[0]

for i in arr:
    if i>max:
        second_max=max
        max=i
    elif i>second_max and i!=max:
        second_max=i

print("Second largest value is :", second_max)