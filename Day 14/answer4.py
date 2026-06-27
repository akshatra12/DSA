# Average of Every Window
def avg(arr):
    w=3
    sum=0
    for i in range(w):
        sum+=arr[i]
    avg=sum/w
    print(avg)
    for i in range(1,len(arr)-w+1):
        sum=sum-arr[i-1]+arr[i+w-1]
        avg=sum/w
        print(avg)
        

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    avg(arr)
