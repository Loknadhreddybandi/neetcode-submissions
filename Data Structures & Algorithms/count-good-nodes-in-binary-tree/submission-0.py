# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root,float('-inf')))
        res = 0
        while queue:
            node,maxvalue = queue.popleft()
            if node.val>=maxvalue:
                res +=1
            if node.left:
                queue.append((node.left,max(node.val,maxvalue)))
            if node.right:
                queue.append((node.right,max(node.val,maxvalue)))
        return res
        