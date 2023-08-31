###This Example is the best way To think in reccursive way 

Man I love reccursive Algorithms They Kinda Give Us the sense of what is possibe with computers



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left,right):

            if not left and not right:
                return True
            if not left or not right:
                return False
            

            return (
                left.val==right.val and
                dfs(left.left,right.right) and

                dfs(left.right,right.left)

            )
        
        return dfs(root.left,root.right)
