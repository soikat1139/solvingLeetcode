def reachLeafNode(root,path):
  if not root or root.val==0:
    return False
    path.append(root.val)
  if not root.left and not root.right:
    return True
  if reachLeafNode(root.left):
    return True
  if reachLeafNode(root.right):
    return True
  path.pop()
  return False
