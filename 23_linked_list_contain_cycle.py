class LinkedListNode:
    """linked list node"""
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def insert(self, data):
        self.next = LinkedListNode(data, self.next)
        # create cyle
        if data == 3:
            self.create_cycle(self)
        return self.next

    def showall(self):
        print self.__dict__
        if self.next != None:
            self.next.showall()

    def create_cycle(self, cycle):
        self.next = cycle

    def contains_cycle(self, first_node):
        slow_runner = first_node
        fast_runner = first_node
        while fast_runner != None and fast_runner.next !=None:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
            if fast_runner == slow_runner:
                return True
        return False

ll = LinkedListNode(1)
ll.insert(2).insert(3).insert(4).insert(5).insert(6).insert(7).insert(8).insert(9).insert(10)
# ll.showall()
print ll.contains_cycle(ll)