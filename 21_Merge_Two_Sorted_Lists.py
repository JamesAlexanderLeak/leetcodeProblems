from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

        Return the head of the merged linked list.
        """
        #create initial node and dummy pointer to initial node
        currentNode = dummyNode = ListNode()
        #while both lists exist
        while list1 and list2:
            #if list1 is less than list2 val
            if list1.val < list2.val:
                #currentNode.next is list1 (append list1 to current)
                currentNode.next = list1
                #list1 is equal to the next value in the list, currentNode is equal to next val in list
                list1, currentNode = list1.next, list1
            else:
                #currentNode.next is list2 (append list 2 to current)
                currentNode.next = list2
                #list 2 is equal to next in list, current node is equal to list2, this is done in case empty list.
                list2, currentNode = list2.next, list2
        #if one list is ended, append the rest of the other list to currentNode.    
        if list1 or list2:
            currentNode.next = list1 if list1 else list2
        #return dummyNode.next which is the head node of the new linked list.
        return dummyNode.next
        