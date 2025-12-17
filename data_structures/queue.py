class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise IndexError("Очередь пустая!")
        return self.items.pop(0)

    def front(self):
        if not self.items:
            raise IndexError("Очередь пустая!")
        return self.items[0]

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)
