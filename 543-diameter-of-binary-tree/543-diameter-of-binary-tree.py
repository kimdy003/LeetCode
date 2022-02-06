# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    
    def dfs(self, node):
        if node is None:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.ans = max(self.ans, left + right)
        
        return max(left, right) + 1
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        
        return self.ans