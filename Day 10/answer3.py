# Sum of Array
def find_sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
if __name__ == "__main__":
    arr=[1,2,3,4,5]
    print(find_sum(arr))