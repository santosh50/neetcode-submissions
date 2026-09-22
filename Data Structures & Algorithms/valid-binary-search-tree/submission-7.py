# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def valid(self, root: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
        if not root:
            return True
        if not (minVal < root.val < maxVal):
            return False
        return self.valid(root.left, minVal, root.val) and self.valid(root.right, root.val, maxVal)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))
        