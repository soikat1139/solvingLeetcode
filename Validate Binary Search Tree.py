# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res=[]

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        def is_Sorted(arr):
            if not arr:
                return False
            for i in range(1,len(arr)):
                if arr[i]<=arr[i-1]:
                    return False
            return True
        
        return is_Sorted(res)
