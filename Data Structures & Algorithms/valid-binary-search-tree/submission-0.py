# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(node, minNum, maxNum):
            if not node:
                return True
            
            if node.val <= minNum or node.val >= maxNum:
                return False
            
            return helper(node.left, minNum, node.val) and helper(node.right, node.val, maxNum)
        return helper(root, float('-inf'), float('inf'))