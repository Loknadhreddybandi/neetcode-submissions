# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def traverse(node):
            if not node:
                return
            heapq.heappush(heap, node.val)  # min heap
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        for _ in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
        


        
        