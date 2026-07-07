# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #start at the first node of each list. 
        #the list that is being added in will compare with first of stable list
        #if its the same number put it as its head.
        #if its more then move onto the second number and compare it.

        list3 = ListNode()
        curr = list3
        while list1 and list2 :

            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
                
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return list3.next
        