#Maximum Sum of Window Size 3
def max_sum(arr):
    w=3
    sum=0
    for i in range(w):
        sum+=arr[i]
    max_sum=sum
    for i in range(1,len(arr)-w+1):
        sum=sum-arr[i-1]+arr[i+w-1]
        if sum>max_sum:
            max_sum=sum
    return max_sum
    


if __name__ == "__main__":
    arr= [2,1,5,1,3,2]
    print(max_sum(arr))
