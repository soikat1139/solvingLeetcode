


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':


        oldTonew={}

        def dfs(node):
            if node in oldTonew:
                return oldTonew[node]
            
            copy=Node(node.val)

            oldTonew[node]=copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node) if node else node

