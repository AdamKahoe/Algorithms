class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        first = head.next
        second = head
        second.next = self.swapPairs(first.next)
        first.next = second
        return first