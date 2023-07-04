#Implementing adjacency List
class GroupNode:
  def __init__(self,val):
    self.val=val
    self.neighbhor=[]

#Or hashMap Can be used to implement adjacency List:

edges=[["A","B"],["B","C"],["B","E"],["C","E"],["E","D"]]

adjList={}

for src,dst in edges:
    if src not in adjList:
        adjList[src]=[]
    if dst not in adjList:
        adjList[dst]=[]
    adjList[src].append(dst)


print(adjList)


