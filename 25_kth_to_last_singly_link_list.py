class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

def kth_to_last_node(head, k):
        count = 1
        k_pointer = head
        while head.next:
            if count >= k:
                k_pointer = k_pointer.next
            else:
                count += 1
            head = head.next
        return k_pointer.value

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e
print kth_to_last_node(a,2)