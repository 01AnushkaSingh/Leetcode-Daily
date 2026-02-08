# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced.
        A height-balanced tree is defined as a tree where the depth of the two subtrees 
        of every node never differs by more than 1.
      
        Args:
            root: The root node of the binary tree
          
        Returns:
            True if the tree is balanced, False otherwise
        """
      
        def calculate_height(node: Optional[TreeNode]) -> int:
            
           
            if node is None:
                return 0
          
            
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
          
           
            if (left_height == -1 or 
                right_height == -1 or 
                abs(left_height - right_height) > 1):
                return -1  
          
            
            return 1 + max(left_height, right_height)
      
        
        return calculate_height(root) >= 0
