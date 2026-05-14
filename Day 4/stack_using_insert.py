class Stack:
    def __init__(self) -> None:
        self.lists = []

    def length(self):
        return len(self.lists)

    def isEmpty(self):
        return len(self.lists) == 0

    # push keeps the new element on index 0
    def push(self, value):
        self.lists.insert(0, value)  # no need to check isEmpty for push

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.lists.pop(0)

    def traverse(self):
        for item in reversed(self.lists):
            print(item)


stk = Stack()
stk.push(10)
stk.push(10)
stk.push(10)
print(stk.length())
stk.traverse()
