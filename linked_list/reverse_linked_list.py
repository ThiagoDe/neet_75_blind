class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            nextN = current.next # temp val to save next
            current.next = prev # reasign next to prev
            prev = current # prev is now current for the next iteration

            current = nextN # current is the next saved in a temporary variable

        return prev
