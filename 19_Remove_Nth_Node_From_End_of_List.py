# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
        """
        #use slow/fast pointer method to iterate through list n number of times.
        slow=fast=head
        #iterate through linked list n number of times
        for _ in range(n):
            fast = fast.next
        if fast ==None:
            return head.next
        # while not at end of list, move forward
        while fast.next:
            slow = slow.next
            fast = fast.next
        #remove nth node
        slow.next = slow.next.next
        #return head
        return head