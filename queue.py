class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_data(self):
        return self.data


class Queue:
    def __init__(self):
        self.front_node = None
        self.back_node = None
        self.length = 0

    def peek(self):
        if self.is_empty():
            print("empty queue")
        else:
            return self.front_node.get_data()

    def checked_en(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front_node = new_node
            self.back_node = new_node
        else:
            self.back_node.set_next_node(new_node)
            self.back_node = new_node
        self.length += 1

    def enqueue(self, data):
        if data > 12:
            my_data = data
            counter = 1
            while my_data > 12:
                my_data -= 12
                counter += 1
            while counter != 1:
                self.checked_en(12)
                counter -= 1
            if my_data != 0:
                self.checked_en(my_data)
        else:
            self.checked_en(data)

    def dequeue(self):
        if self.is_empty():
            print("empty queue")
        else:
            removed_node = self.front_node
            if self.get_length == 1:
                self.front_node = None
                self.back_node = None
            else:
                self.front_node = removed_node.get_next_node()
            self.length -= 1
            return removed_node.get_data()

    def is_empty(self):
        return self.length == 0

    def get_length(self):
        return self.length

    def get_waiting_time(self):
        return self.length*0.5

park_queue = Queue()
print("waiting time: %s"%(park_queue.get_waiting_time()))
park_queue.enqueue(16)
park_queue.enqueue(12)
park_queue.enqueue(8)
park_queue.enqueue(7)
print("waiting time: %s"%(park_queue.get_waiting_time()))
print("the group of %s come in"%(park_queue.dequeue()))
print("waiting time: %s"%(park_queue.get_waiting_time()))
