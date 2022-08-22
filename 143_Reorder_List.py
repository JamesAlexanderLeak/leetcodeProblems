from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        You are given the head of a singly linked-list. The list can be represented as:
        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.        
        """
        #slow and fast moving through linked list.
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #should work so that when fast reaches end of list, slow is in middle
        second = slow.next
        prev = slow.next = None
        #reverse second half of list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first,second = head,prev
        #merge lists
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2