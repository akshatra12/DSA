# Minimum Sum Window
def min_sum(arr):
    w=2
    sum=0
    for i in range(w):
        sum+=arr[i]
    min_sum=sum
    for i in range(1,len(arr)-w+1):
        sum=sum-arr[i-1]+arr[i+w-1]
        if sum<min_sum:
            min_sum=sum
    return min_sum
if __name__ == "__main__":
    arr = [4,2,1,7,8]
    print(min_sum(arr))