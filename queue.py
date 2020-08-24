class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class Queue:
    def __init__(self, limit=10, front=None, back=None):
        self.front = front
        self.back = back
        self.limit = limit
        self.length = 0


    def is_full(self):
        return self.length == self.limit

    def peek(self):
        return self.front

    def is_empty(self):
        return self.length == 0

    def enqueue(self, data):
        if self.is_full():
            print("no space!")
        else:
            new_node = Node(data)
            if self.is_empty():
                self.front = new_node
            else:
                self.back.set_next(new_node)
            self.back = new_node
            self.length += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            removed_node = self.front
            self.front = removed_node.get_next()
            self.length -= 1
            return removed_node.get_data()



first_room = Queue()

first_room.enqueue("khalid")
first_room.enqueue("ahmed")
first_room.enqueue("mohammed")
first_room.enqueue("gfhsgh")
first_room.enqueue("dfgdgh")
first_room.enqueue("njjkdgtj")
first_room.enqueue("sfjfrhj")
first_room.enqueue("jyutkyukuk")
first_room.enqueue("nj")
first_room.enqueue("sfjfrh")
first_room.enqueue("jyutkyuku")


print(first_room.dequeue())
print(first_room.dequeue())
print(first_room.dequeue())
print(first_room.dequeue())
print(first_room.dequeue())
print(first_room.dequeue())
print(first_room.dequeue())
print(first_room.dequeue())
print(first_room.dequeue())
