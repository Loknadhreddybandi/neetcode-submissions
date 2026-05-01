# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(root):
            if not root:
                return 0
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0) #this is like if any subtree either left or right has sum negative return 0
            nonlocal res
            res = max(res, left+right+root.val)
            return root.val + max(left,right)
        dfs(root)
        return res        