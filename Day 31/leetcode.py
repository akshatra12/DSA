#leetcode:

# observation: we need to remove duplicate from the array
# pattern: we use hash set and hashing
# why? : because hash set and hashing are used to find the find duplicates
#brute force hashing (using dictinory)
# case 1:
def remove_duplicate(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq.keys()
nums = [1,1,2]
print(remove_duplicate(nums))

# case 2:
def remove_duplicate(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq.keys()
nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicate(nums))


#better Approach(hash set)
# case 1:
def remove_duplicate(nums):
    seen=set()
    for i in nums:
        if i not in seen:
            seen.add(i)
    return seen
nums = [1,1,2]
print(remove_duplicate(nums))

# case 2:
def remove_duplicate(nums):
    seen=set()
    for i in nums:
        if i not in seen:
            seen.add(i)
    return seen
nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicate(nums))
