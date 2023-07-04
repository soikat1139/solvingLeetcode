def dfs(node,target,adjList,visit):

    if node==target:
        return 1
    if node in visit:
        return 0
    count=0
    visit.add(node)

    for neighbhor in adjList[node]:
        count+=dfs(neighbhor,target,adjList,visit)
    visit.remove(node)

    return count
print(dfs("A","E",adjList,set()))
