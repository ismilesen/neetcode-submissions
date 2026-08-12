# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [float('-inf')]
        def dfs(node):
            if not node:
                return 0 
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            currentPath = node.val + left + right

            maxSum[0] = max(maxSum[0], currentPath)

            return node.val + max(left, right)


        dfs(root) 
        
        return maxSum[0]