This problem is a gem itself.I love this problem .This is the kind of problem that keeps you alive..........

This is the first solution that has 0(n^2) time complexity

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root=TreeNode(postorder.pop())

        idx=inorder.index(root.val)

        root.right=self.buildTree(inorder[idx+1:],postorder)
        root.left=self.buildTree(inorder[:idx],postorder)
        return root

  ###Most optimal Solution
