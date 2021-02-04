class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if not str(item).isspace():
            self.items.append(item)

    def pop(self, index=-1):
        return self.items.pop(index)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)