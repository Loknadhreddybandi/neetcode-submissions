# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap =[]
        dummy = ListNode(-1)
        curr = dummy
        for k,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,k,node))
        while heap:
            val,k,node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap,(node.next.val,k,node.next))
        return dummy.next

        