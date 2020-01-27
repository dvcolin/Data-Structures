from dll import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.tail:
            value = self.storage.tail.value
            self.size -= 1
            self.storage.remove_from_tail()
            return value
        else:
            return None

    def len(self):
        return self.size
