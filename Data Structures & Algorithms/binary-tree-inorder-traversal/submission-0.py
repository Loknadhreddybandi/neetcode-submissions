# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        def in_order_traversal(root):
            if not root:
                return []
            in_order_traversal(root.left)
            order.append(root.val)
            in_order_traversal(root.right)

        in_order_traversal(root)
        return order
            
        