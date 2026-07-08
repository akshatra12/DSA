def max_subsum(arr):
    current_sum=0
    max_sum=arr[0]
    for num in arr:
        current_sum+=num
        if max_sum<current_sum:
            max_sum=current_sum
        if current_sum<0:
            current_sum=0
    return max_sum
arr = [-1,-2,-3,-4]
print(max_subsum(arr))