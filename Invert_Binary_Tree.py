# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverseTree(root):
           if not root:
             return
   

           temp=root.right
           root.right=root.left 
           root.left=temp

           reverseTree(root.right)
           reverseTree(root.left)
        reverseTree(root)
        return root

#To solve this problem you will need to understand recurrsion properly.
#Here Is how you solve reccursion

