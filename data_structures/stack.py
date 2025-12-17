class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Стек пустой!")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("Стек пустой!")
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)
