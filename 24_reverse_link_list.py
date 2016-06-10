'''
Write a function for reversing a linked list . Do it in-place .
'''


class LinkedListNode:

    def __init__(self,value):
        self.value = value
        self.next = None

    def reverse_list(self, head):
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

    def printList(self,head):
        while head is not None:
            print head.value
            head = head.next

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)
e = LinkedListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

print e.printList(a)
head = e.reverse_list(a)
e.printList(head)


