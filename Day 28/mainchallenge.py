# main Challenge

# Observation:first we find the largest the we find the second largest

# Pattern:traverse the array two times

# Algorithm:

# 1.initialize largest=0 and second_largest=-1
# 2.traverse the array
# 3.check if arr[i]>largest then update largest
# 4.repeat untill we find the largest element
# 5.again traverse the array
# 6.now check arr[i]>second_largest and arr[i]!=largest
# 7. update second_largest
# 9 repeat untill we find second largest
# 10. return second_largest

# Time Complexity:O(n)

# Space Complexity:O(1)

# code:
def find_second_largest(arr):
    largest=0
    second=0
    for i in range(len(arr)):
        if arr[i]>largest:
            second=largest
            largest=arr[i]
        elif arr[i]>second and arr[i]<largest:
            second=arr[i]
    return second
arr = [8,3,5,1,9,6]
print(find_second_largest(arr))
