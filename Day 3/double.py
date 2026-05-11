# Double linked list

class Node:
    def __init__(self, info=None):
        self.prev = None
        self.info = info
        self.next = None


class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_end(self, value):
        new_node = Node(value)

        # empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        current = self.head

        # move to last node
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

        self.tail = new_node

    def append_start(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def travel(self):
        current = self.head

        while current:
            if current.next:
                print(f"[{current.info}] <-> ", end="")
            else:
                print(f"[{current.info}]")

            current = current.next

    def search(self, value):
        current = self.head
        pos = 0
        while current:
            if current.info == value:
                return pos
            current = current.next
            pos += 1
        return -1

    def counter(self, value):
        current = self.head
        count = 0
        while current:
            if current.info == value:
                count += 1
            current = current.next
        print(f"count number of accurence : {count}")

    def append_at(self, value, pos):

        current = self.head
        new_node = Node(value)

        while current:
            if current.info == pos:
                new_node.next = current.next
                new_node.prev = current

                if current.next:
                    current.next.prev = new_node

                current.next = new_node

                # update tail if inserted at end
                if new_node.next is None:
                    self.tail = new_node
                return

            current = current.next


n1 = DoubleLL()

n1.append_end(10)
n1.append_end(20)
n1.append_end(10)
n1.append_end(20)
n1.append_end("dosa")

n1.travel()

n1.append_start(200)
n1.travel()
print(n1.search(20))
n1.counter(1)
