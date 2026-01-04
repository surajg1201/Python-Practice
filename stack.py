class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Underflow")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Overflow")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack)
print("Top element:", stack.peek())
print("Stack size:", stack.size())
print("Popped element:", stack.pop())
print("Stack after pop:", stack)
