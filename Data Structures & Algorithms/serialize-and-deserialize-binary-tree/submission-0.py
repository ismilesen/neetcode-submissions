# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string iteratively using Pre-order DFS."""
        if not root:
            return "null"
            
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node is None:
                res.append("null")
            else:
                res.append(str(node.val))
                # Push right child first so left child is processed first (LIFO stack)
                stack.append(node.right)
                stack.append(node.left)
                
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to a tree iteratively using a stack."""
        if data == "null" or not data:
            return None
            
        values = data.split(",")
        root = TreeNode(int(values[0]))
        
        # Stack stores tuples of: (parent_node, child_type)
        # child_type: 0 for left child, 1 for right child
        stack = [(root, 1), (root, 0)]
        
        # Start reading values from index 1
        for val in values[1:]:
            parent, child_type = stack.pop()
            
            if val != "null":
                new_node = TreeNode(int(val))
                
                # Attach the node to its parent
                if child_type == 0:
                    parent.left = new_node
                else:
                    parent.right = new_node
                    
                # Push its future children configurations to the stack
                # Right child setup goes first, then Left child setup
                stack.append((new_node, 1))
                stack.append((new_node, 0))
                
        return root

