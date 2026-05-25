class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def push(self, value):
        self.items.append(value)
        return f"Pushed to stack : {value}"


s = Stack()
s.push(10)
print(s.push(20))
print(s.pop())  # 20
print(s.pop())  # 10
# print(s.pop())  # Exception: Stack is empty
