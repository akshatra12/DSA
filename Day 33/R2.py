# R2
from collections import deque
def check_duplicate(arr):
    queue=deque()
    seen=set()
    found=False
    for i in arr:
        if i in seen:
            if found ==False:
                found=True
                print(f"first duplicate is {i}")
                 
        else:
            seen.add(i)
            queue.append(i)
    return queue ,len(queue)
arr = [3,5,3,2,7,2,8]
print(check_duplicate(arr))