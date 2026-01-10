# class Linkdedlist:
#     def __init__(self, value):
#         new_node = Node(value) #O(1)
#         self.head = new_node #O(1)
#         self.tail = new_node #O(1)
#         self.length = 1 #O(1)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkdedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

linked_list = Linkdedlist()
linked_list.append(20)
linked_list.append(202)
print(linked_list.head.value, linked_list.tail.value)
print(linked_list.length)