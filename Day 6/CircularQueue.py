class CircularQueue:
    def __init__(self, size=6):
        self.items = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        # Queue full
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full"

        # First element
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.items[self.rear] = value

    def dequeue(self):
        # Queue empty
        if self.front == -1:
            return "Queue is empty"

        removed = self.items[self.front]
        self.items[self.front] = None

        # Last element removed
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return removed

    def traverse(self):
        if self.front == -1:
            print("Queue is empty")
            return

        i = self.front

        while True:
            print(self.items[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


cq = CircularQueue(10)
for i in range(30, 100):
    cq.enqueue(i)
cq.enqueue(10)
cq.traverse()
cq.dequeue()
cq.traverse()
