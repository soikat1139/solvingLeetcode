# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res=[]
        q=collections.deque()
        if root:
            q.append(root)
        

        while q:
            
            level=[]

            

            for i in range(len(q)):
                curr=q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if level:
                 res.append(level[-1])
        return res
