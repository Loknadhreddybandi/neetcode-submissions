# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        result = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
        
            # pop and process
            curr = stack.pop()
            result.append(curr.val)
            
            # move to right
            curr = curr.right
        
        return result
        