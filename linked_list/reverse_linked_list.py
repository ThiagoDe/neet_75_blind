class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            nextN = current.next
            current.next = prev
            prev = current

            current = nextN

        return prev
