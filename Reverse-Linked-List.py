# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        def reverse(root,prev=None):
            if not root:
                return prev
            temp=root.next
            root.next=prev

            return reverse(temp,root)
        return reverse(head)
        
