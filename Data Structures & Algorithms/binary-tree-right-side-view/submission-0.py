# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #go through layers
        #check if node.left exists and if node.right exists
        #if node.left but no node.right then node.left is visible
        #if node.right then right is visible regardless of left node
        #bfs
        #alternatively using the queue 
        #whatever is on top should be able to be popped before last is disregarded and final is added to list as visible
        #take list only append the final element


        res = []
        q = collections.deque([root])
        

        while q:
            qLen = len(q)
            visNode = None

            for element in range(qLen):
    
                node = q.popleft()
              
                if node:
                    visNode = node
                    q.append(node.left)
                    q.append(node.right)
                    
            if visNode:
                res.append(visNode.val)

        return res