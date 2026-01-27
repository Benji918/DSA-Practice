class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # 1. Find mid (end of first half)
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # now slow is at end of first half

        # 2. Reverse second half starting at slow.next
        second_start = self.reverse_list(slow.next)

        # 3. Compare first half and reversed second half
        p1 = head
        p2 = second_start
        result = True
        while p2 is not None:   # only need to compare length of second half
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next

        # 4. (Optional) Restore the original list by reversing second half again
        slow.next = self.reverse_list(second_start)

        return result


    def reverse_list(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        return prev