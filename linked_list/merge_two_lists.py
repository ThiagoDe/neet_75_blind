# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode() # used to append will be returned at the end
        tail = dummy # will change everytime tail is set to tail.next

        while l1 and l2: # both have to exist 
            if l1.val < l2.val: # acd
                tail.next = l1  # 
                l1 = l1.next #update l1
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # make sure if we have linked List of diff lengths that the rest will be added to the and of the new list
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next

#             tail = tail.next

#         if l1:
#             tail.next = l1
#         if l2:
#             tail.next = l2

#         return dummy.next
