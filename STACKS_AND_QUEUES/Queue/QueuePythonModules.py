# Creating Queue using Python Modules

# 1. Using Collection module

# from collections import deque

# customQueue = deque(maxlen=3)

# customQueue.append(1)
# customQueue.append(2)
# customQueue.append(3)
# customQueue.append(4) # 1 is deleted and shifting is done to make space for 4

# print(customQueue.popleft())

# print(customQueue)

# customQueue.clear()
# print(customQueue)

# 2. Using Queue module
# NOTE: Using this we can create FIFO, LIFO Queue(Stack) and Priority Queue
# But for now we are using FIFO

# import queue as q

# # providing maxsize=0 means infinite cells
# customQueue = q.Queue(maxsize=3)
# print(customQueue.empty()) # returns True

# print(customQueue.qsize()) # return 0 as no element is inserted yet
# customQueue.put(1)
# customQueue.put(2)
# customQueue.put(3)

# print(customQueue.qsize()) # returns 3 as three elements are added
# print(customQueue.empty()) # returns False
# print(customQueue.get()) # returns 1 and is being deleted
# print(customQueue.qsize()) # returns 2

# 3. Using Multiprocessing module
# NOTE: This module is used to create Queue so that it can be shared and can be stored for further use
# How to use multiprocessing.Queue as a FIFO queue:
from multiprocessing import Queue

customQueue = Queue(maxsize=3)
print(customQueue.qsize())

# NOTE: Methods are almost same as Queue module except task_done() and join() methods are not used over here
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize())

print(customQueue.get()) # returns 1 and it is being deleted
print(customQueue.qsize())