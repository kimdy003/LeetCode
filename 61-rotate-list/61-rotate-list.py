# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        lastNode = head
        length = 1
        
        while lastNode.next:
            lastNode = lastNode.next
            length += 1
        
        lastNode.next = head
        k = k % length
        
        tempNode = head
        for _ in range(length - k -1):
            tempNode = tempNode.next
            
        ans = tempNode.next
        tempNode.next = None
        
        return ans
        