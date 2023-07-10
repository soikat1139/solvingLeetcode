# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res=[]

        curr=head

        while curr:
            res.append(curr.val)
            curr=curr.next
        res.sort()

        curr2=head
        for n in res:
            curr2.val=n
            curr2=curr2.next
        return head
