# Largest Element
arr=[12,45,7,89,23]

larger = arr[0]

for i in arr:
    if i>larger:
        larger=i

print("larger number is" , larger)