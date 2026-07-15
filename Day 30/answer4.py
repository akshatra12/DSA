# 1
from collections import deque
queue=deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)

#2
print(queue.popleft())
print(queue)

#3
print(f"front is {queue[0]}")

#4
print(f"rear is {queue[-1]}")

