# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#have a pointer go to n + 1 index
#have a pointer go to n - 1 index
#have the tail of n - 1 become head of n+1

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        rPointer = dummy
        lPointer = dummy
        countR = 0
        countL = 0
        while countR < n and rPointer.next:
            rPointer = rPointer.next
            countR += 1
        while rPointer.next:
            rPointer = rPointer.next
            lPointer = lPointer.next

        lPointer.next = lPointer.next.next

        return dummy.next