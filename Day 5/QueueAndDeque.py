from collections import deque


class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return len(self.item) == 0

    def inque(self, value):
        self.item.append(value)

    def deque(self):
        if not self.isEmpty():
            return self.item.pop(0)
        return None


class DoubleQueue:
    def __init__(self):
        self.item = deque()

    def inque_at_start(self, value):
        self.item.appendleft(value)

    def inque_at_end(self, value):
        self.item.append(value)

    def deque_at_start(self):
        if self.item:
            return self.item.popleft()
        return None

    def deque_at_end(self):
        if self.item:
            return self.item.pop()
        return None


# Test Queue
q = Queue()
print(q.item)
print(q.isEmpty())
q.inque(10)
q.inque(12)
q.inque(20)
print(q.isEmpty())
print(q.item)
q.deque()
print(q.item)

# Test DoubleQueue
dq = DoubleQueue()
dq.inque_at_end(1)
dq.inque_at_start(0)
dq.inque_at_end(2)
print(dq.item)
dq.deque_at_start()
dq.deque_at_end()
print(dq.item)
