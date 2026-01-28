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

    def traverse(self):
        current = self.head
        for _ in range(self.length):
            print(current.value)
            current = current.next


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


    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0 or self.head is None and self.tail is None:
            self.head = new_node
            new_node.next = self.head
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1


    def search(self, value):
        current = self.head
        index = 0
        for _ in range(self.length):
            if current.value == value:
                return True, index
            current = current.next
            index += 1
        return False


    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError('Index out of bounds!')

        if index == 0:
            self.prepend(value)
            return

        if index == self.length:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head
        prev = None


        for _ in range(index -1):
            prev = current
            current = current.next

        prev.next = new_node
        new_node.next = current

        self.length += 1


cslinkedlist = CSLinkedList(1)
cslinkedlist.append(2)
cslinkedlist.append(3)
cslinkedlist.append(3)
cslinkedlist.prepend(45)
cslinkedlist.prepend(45)
cslinkedlist.insert(3,40)
print(cslinkedlist.search(40))

print(cslinkedlist.display())