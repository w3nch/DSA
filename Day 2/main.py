# Singly linked list
class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_at_start(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def append_after(self, target, value):
        current = self.head

        # find target
        while current is not None and current.info != target:
            current = current.next

        if current is None:
            print("Value not found")
            return

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

        # update tail if inserted at end
        if new_node.next is None:
            self.tail = new_node

    def insert_before_value(self, target, value):
        new_node = Node(value)

        # empty list
        if self.head is None:
            print("List is empty")
            return

        # target at head
        if self.head.info == target:
            new_node.next = self.head
            self.head = new_node
            return

        prev = None
        current = self.head

        while current is not None and current.info != target:
            prev = current
            current = current.next

        if current is None:
            print("Value not found")
            return

        prev.next = new_node
        new_node.next = current

    def print_list(self):
        current = self.head

        while current is not None:
            print(f"[{current.info}]->", end="")
            current = current.next

        print("None")


# TEST
f = LinkedList()

f.append_at_end(10)
f.append_at_start(20)

first_list = [1, 2, 3, 4, 5]
for i in first_list:
    f.append_at_end(i)

f.append_after(20, 30)
f.insert_before_value(10, 99)

f.print_list()
