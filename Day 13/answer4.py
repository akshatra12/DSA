#Count Swaps
def swap_count(arr):
    count=0
    left=0
    right=len(arr)-1
    while left<right:
        left+=1
        right-=1
        count+=1
    return count
arr=[1,2,3,4,5,6]
print(swap_count(arr))