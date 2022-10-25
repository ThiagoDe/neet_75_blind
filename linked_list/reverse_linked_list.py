class Solution:
    def reverseList(self, head):  # 1 -> 2 -> 3 -> 4 -> 5 ->
                            #prv  curr tpNxt
        # start with two pointers prev and current 
        prev = None 
        current = head

        #iterate through the entire list
        # before reasign current.next 
        while current: # 1 
            nextN = current.next # temp val to save next = 2
            current.next = prev # reasign next to prev  break -> 2 | -> None
            prev = current # prev is now current for the next iteration prev = 1 

            current = nextN # current is the next saved in a temporary variable current = 2

        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
