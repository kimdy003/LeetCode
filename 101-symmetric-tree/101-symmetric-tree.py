# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left : TreeNode, right : TreeNode) -> bool:
                if left == None and right == None:
                    return True
                elif left == None or right == None:
                    return False
                
                return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        
        return check(root.left, root.right)