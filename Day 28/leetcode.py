# leetcode

# find duplicate using hashing

# case1:
def check_duplicate(nums):
    freq={}
    for i in nums:
        if i in freq:
            return True
        else:
            freq[i]=1
    return "no duplicate"
nums = [1,2,3,1]
print(check_duplicate(nums))

# case2

nums = [1,2,3,4]
print(check_duplicate(nums))

# case3:

nums = [1,1,1,3,3,4]
print(check_duplicate(nums))