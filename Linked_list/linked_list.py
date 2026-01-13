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

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

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

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, value):
        current = self.head
        index = 0

        while current:
            if current.value == value:
                return f'Search value -> {value}', f'Value index -> {index}'
            current = current.next
            index += 1

        return None

    def get(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer!')

        if index < 0:
            index = self.length + index # support negative indexing


        if index >= self.length:
            raise IndexError('Index out of bounds!')

        linkded_list_index = 0
        current = self.head

        for _ in range(index):
            if linkded_list_index == index:
                break

            linkded_list_index += 1
            current = current.next

        return current

    def set_value(self, index, value):
        get_value = self.get(index)
        if get_value is not None:
            get_value.value = value

            return True

        return False

    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            return self.pop_first()
        else:
            self.tail = self.get(self.length - 2)
            self.tail.next = None

        self.length -= 1


    def pop_first(self):
        if self.length == 0:
            return None

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        popped_node.next = None
        self.length -= 1

        return popped_node.value



linked_list = Linkdedlist()
linked_list.append(20)
linked_list.append(202)
linked_list.append(2024)
linked_list.prepend(10)
linked_list.prepend(10)

linked_list.insert(0, 15)
# linked_list.traverse()
# print(linked_list.search(201))
# print(linked_list.get(-3))
# print(linked_list.set_value(index=-3, value=999))
# print(linked_list.pop_first())
# print(linked_list.length)
print(linked_list)
print(linked_list.pop())
print(linked_list)