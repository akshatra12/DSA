#R1
# Observation: we need to find first duplicate element from the array and then store all the unique elements in the queue
# pattern:hash Set + queue
# Time Complexity:O(n)
# space complexity:O(n)
from collections import deque
def find_duplicate(arr):
    queue=deque()
    seen=set()
    found=True
    for num in arr:
        if num in seen:
            if found==True:
                print(num)
                found=False
        else:
            seen.add(num)
            queue.append(num)
    return queue
arr = [4,1,4,2,3,2,5]
print(find_duplicate(arr))