class Myqueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("overflow")
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("underflow")
        self.__queue.pop(0)

    def font(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.__queue[0]


my_queue = Myqueue(5)
my_queue.is_empty()
my_queue.is_full()
my_queue.enqueue(5)
my_queue.enqueue(10)
print(my_queue.dequeue())
print(my_queue.font())
