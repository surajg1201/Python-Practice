from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self):
        return self.q[-1]

    def empty(self):
        return len(self.q) == 0


s = MyStack()

s.push(10)
s.push(20)
s.push(30)

print("Top:", s.top())
print("Pop:", s.pop())
print("Top after pop:", s.top())
print("Is Empty:", s.empty())
