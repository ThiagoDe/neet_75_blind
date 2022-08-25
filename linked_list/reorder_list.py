class Solution:
    def reorderList(self, head):
        # set two pointers to find the middle node and the last node
        slow, fast = head, head.next 
        # 1 -> 2 -> 3 -> 4 -> 5
        #           s        f   f.next
        # 1 -> 2 -> 3 -> 4 -> 
        #      s         f   f.next
        while fast and fast.next: # until fast.next is None
            slow = slow.next
            fast = fast.next.next

        # the head of the second part is slow(last from the first half) .next 
        second = slow.next # cache in a temp
        # use to pointers to 
        slow.next = prev = None # set the last node of first haft points to None 

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev


        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
