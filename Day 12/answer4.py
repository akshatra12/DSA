#Count Frequency

def Count(arr,target):
    count=0
    for i in arr:
        if i==target:
            count+=1
    return count

arr=[5,2,5,8,5,10]
target=int(input("Enter the target number to count: "))
result=Count(arr,target)
print(f"The number {target} appears {result} times in the array.")