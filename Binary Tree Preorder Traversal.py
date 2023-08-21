# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        preOrders=[]


        def preOrder(root,preOrders):
            if not root:
                return
            
            preOrders.append(root.val)

            preOrder(root.left,preOrders)
            preOrder(root.right,preOrders)
        
        preOrder(root,preOrders)

        return preOrders

            
