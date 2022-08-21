from typing import List,Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        """

        #typical linked list reversal
        #set prev node to none, cur node to head.
        prevNode = None
        curNode = head
        #while curNode is not None, set nextNode = curNode.next,
        #curNode.next to prev Node, prevNode to curNode and curNode to nextNode.
        while curNode != None:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        #return prevNode which will be the "tail" of the original list
        return prevNode
    