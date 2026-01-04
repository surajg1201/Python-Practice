class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.data

    def print_queue(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:")
queue.print_queue()

print("Front element:", queue.peek())

print("Dequeued element:", queue.dequeue())
print("Queue after dequeue:")
queue.print_queue()

print("Dequeued element:", queue.dequeue())
print("Queue after dequeue:")
queue.print_queue()

print("Dequeued element:", queue.dequeue())
print("Queue after dequeue:")
queue.print_queue()
