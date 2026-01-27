class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        if head is None or val is None:
            return

        while head and head.val == val:
            head = head.next

        current_node = head


        while current_node is not None and current_node.next is not None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next


        return head