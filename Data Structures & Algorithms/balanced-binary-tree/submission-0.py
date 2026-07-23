# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
       #start with root. Go all the way left and right. Count left height and right height. lH - Rh abs <= 1
       #then shift the root to the left and do the same thing
       #boolean
       #even one false node means return false for entire tree
        
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balance, 1 + max(left[1], right[1])]
       # leftHeight = dfs(root.left)[0]
        #rightHeight = dfs(root.right)[0]
       # balance = abs(leftHeight - rightHeight)
        return dfs(root)[0]