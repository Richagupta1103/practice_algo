'''
Implement a queue with 2 stacks . Your queue should have an enqueue and a dequeue function and
it should be "first in first out" (FIFO).
'''

class ImplementQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,x):
        self.stack1.append(x)

    def dequeue(self):
        x = None
        if self.stack2:
            x = self.stack2.pop()
        else:
            while self.stack1:
                elem = self.stack1.pop()
                self.stack2.append(elem)
            if self.stack2:
                x = self.stack2.pop()
        print x


obj = ImplementQueue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.dequeue()
obj.enqueue(11)
obj.dequeue()
obj.enqueue(21)
obj.enqueue(31)
obj.enqueue(41)
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()

