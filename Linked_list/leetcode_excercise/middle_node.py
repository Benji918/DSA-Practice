def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def middleNode(self, head):
        current = head
        length = 0

        while current is not None:
            current = current.next
            length += 1

        current = head
        index = int(length // 2)

        for _ in range(index):
            current = current.next

        return current
