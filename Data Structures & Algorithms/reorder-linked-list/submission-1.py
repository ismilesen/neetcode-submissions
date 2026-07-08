# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None
        prev = None
        while list2:
            tmp = list2.next
            list2.next = prev
            prev = list2
            list2 = tmp

        firstHalf = head
        secondHalf = prev

        while secondHalf:
            tmp1, tmp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = tmp1
            firstHalf = tmp1
            secondHalf = tmp2




