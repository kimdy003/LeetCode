"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
    
        q = deque([root])
        while q:
            rightnode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightnode = rightnode, cur
                if cur.right:
                    q.extend([cur.right, cur.left])
        return root
        