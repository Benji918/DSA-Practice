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

    def get(self, index):
        if index >= self.length:
            raise IndexError('Index out of bounds!')

        if index < 0:
            index = self.length + index

        current = self.head
        for _ in range(index):
            current = current.next
        return current


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


    def set_value(self, index, value):
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        if index >= self.length:
            raise IndexError('Index out of bounds!')

        if index < 0:
            index = self.length + index

        get_value = self.get(index)
        if get_value:
            get_value.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None

        temp = self.head
        self.head = self.head.next
        self.length -= 1
        self.tail.next = self.head
        temp.next = None

        return temp.value

    def pop(self):
        if self.length == 0:
            return self.pop_first()

        if self.length == 1:
            self.head = None
            self.tail = None

        temp = self.tail
        value = self.get(self.length - 2)
        self.tail = value
        self.tail.next = self.head
        self.length -= 1

        return temp.value

    def remove(self, index):
        if self.length == 0:
            return self.pop_first()

        if index == self.length:
            return self.pop()

        poppped_node = self.get(index)
        prev_node = self.get(index - 1)

        prev_node.next = poppped_node.next
        poppped_node.next = None

        self.length -=1






cslinkedlist = CSLinkedList(1)
cslinkedlist.append(2)
cslinkedlist.append(3)
cslinkedlist.append(3)
cslinkedlist.prepend(459)
cslinkedlist.prepend(45)
cslinkedlist.insert(3,40)
# print(cslinkedlist.search(40))
# print(cslinkedlist.get(3))
# print(cslinkedlist.set_value(index=3, value=100))
print(cslinkedlist.display())
print(cslinkedlist.remove(2))
# print(cslinkedlist.pop())

print(cslinkedlist.display())