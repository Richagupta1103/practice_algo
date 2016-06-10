'''
Delete a node from a singly-linked list , given only a variable pointing to that node.
'''

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def delete_node(self, pointer):
        if pointer.next:
            pointer.value = pointer.next.value
            pointer.next = pointer.next.next


    def printList(self,head):
        while head is not None:
            print head.value,
            head = head.next


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c
a.printList(a)
print "deleted"
a.delete_node(b)
a.printList(a)
