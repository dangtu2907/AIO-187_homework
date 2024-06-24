class Mystack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise OverflowError("Overflow")
        else:
            self.__stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Underflow")
        else:
            return self.__stack.pop()


mystack = Mystack(5)
print(mystack.is_empty())
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
print(mystack.is_empty())
print(mystack.pop())
