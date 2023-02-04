import queue
from queue import PriorityQueue

pq = queue.PriorityQueue()
# pq = PriorityQueue()
pq.put([1, "hello"])
pq.put([3, "World"])
pq.put([2, "python"])
print(pq.get())
pq.put([1, "哈哈，看我插队"])
print(pq.get())
print(pq.get())
