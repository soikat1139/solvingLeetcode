# Definition for a binary tree node.
class TreeNode:
         def __init__(self, val=0, left=None, right=None):
              self.val = val
              self.left = left
              self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(target)
        if root.val>target:
            root.left=self.insertIntoBST(root.left,target)
        elif root.val<target:
            root.right=self.insertIntoBST(root.right,target)
        return root
