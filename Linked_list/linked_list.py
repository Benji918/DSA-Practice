class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkdedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # the next of the new node points to the previous head
            self.head = new_node # update the head to be the new node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # the next of the current tail points to the new node
            self.tail = new_node # update the tail to be the new node
        self.length += 1

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
            print(prev.value)
            current = current.next
            print(current.value)

        prev.next = new_node
        new_node.next = current

        self.length += 1

    def __str__(self):
        result = []
        node = self.head
        while node is not None:
            result.append(str(node.value))
            node = node.next
        return " -> ".join(result)




linked_list = Linkdedlist()
linked_list.append(20)
linked_list.append(202)
linked_list.append(202)
linked_list.prepend(10)
linked_list.prepend(10)

linked_list.insert(2, 15)

print(linked_list.length)
print(linked_list)  # Output: 20 -> 202