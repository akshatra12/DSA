# Sum of Elements at Even Indexes
arr=[10,20,30,40,50]

sum=0

for i in range(len(arr)):
    if i%2==0:
        sum+=arr[i]
        print(f"{i} -> {sum}")

print(f"total sum of elements at even indexes : {sum}")