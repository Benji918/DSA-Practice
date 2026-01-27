class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        new_node.next = self.head
        self.tail = new_node
        self.length = 1


    def append(self, value):
        new_node = Node(value)

        if self.length == 0 or self.head is None and self.tail is None:
            self.head = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def display(self):
        elements = []
        if not self.head:
            return elements

        current = self.head
        while current.next != self.head:
            elements.append(str(current.value))
            current = current.next
            if current == self.head:
                break
        return ' -> '.join(elements)


cslinkedlist = CSLinkedList(1)
cslinkedlist.append(2)
cslinkedlist.append(3)
cslinkedlist.append(3)
print(cslinkedlist.head.next.value)  # Output: 2

print(cslinkedlist.display())  # Output: [1, 2, 3]