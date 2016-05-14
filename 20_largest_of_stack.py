class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []
        self.max_list = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)
        if not self.max_list:
            self.max_list.append(item)
        elif self.max_list[len(self.max_list)-1] < item:
            self.max_list.append(item)


    # remove the last item
    def pop(self):

        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None
        if self.peek() == self.max_list[len(self.max_list)-1]:
            self.max_list.pop()
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items: return None
        return self.items[len(self.items)-1]

class MaxStack(Stack):
    def get_max(self):
        return self.max_list[len(self.max_list)-1]

obj = MaxStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
print obj.get_max()
obj.pop()
print obj.get_max()
obj.pop()
print obj.get_max()
obj.pop()
obj.pop()
print obj.get_max()



# class MaxStack:
#
#     def __init__(self):
#         self.stack      = Stack()
#         self.maxs_stack = Stack()
#
#     # Add a new item to the top of our stack. If the item is greater
#     # than or equal to the the last item in maxs_stack, it's
#     # the new max! So we'll add it to maxs_stack.
#     def push(self, item):
#         self.stack.push(item)
#         if item >= self.maxs_stack.peek():
#             self.maxs_stack.push(item)
#
#     # Remove and return the top item from our stack. If it equals
#     # the top item in maxs_stack, they must have been pushed in together.
#     # So we'll pop it out of maxs_stack too.
#     def pop(self):
#         item = self.stack.pop()
#         if (item == self.maxs_stack.peek()):
#             self.maxs_stack.pop()
#         return item
#
#     # The last item in maxs_stack is the max item in our stack.
#     def get_max(self):
#         return self.maxs_stack.peek()
#
