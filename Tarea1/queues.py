from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,val):
        self.queue.append(val)
    
    def dequeue(self):
        self.queue.popleft()
    
    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return "The queue is empty"
        
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return len(self.queue) == 0

queue = Queue()
print(f"The queue initialized is {list(queue.queue)}")
print("--------------------------------")
print("Appending Elements")
queue.enqueue(1)
print(list(queue.queue))
queue.enqueue(2)
print(list(queue.queue))
queue.enqueue(3)
print(list(queue.queue))
queue.enqueue(4)
print(list(queue.queue))
print("--------------------------------")
print("Dequeuing elements")
queue.dequeue()
print(list(queue.queue))
queue.dequeue()
print(list(queue.queue))
print("--------------------------------")
print(f"The queue is empty: {queue.empty()}")
print("--------------------------------")
print(f"The front element is {queue.front()}")
print("--------------------------------")
print(f"The size of the queue is: {queue.size()}")
print("--------------------------------")
