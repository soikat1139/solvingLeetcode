class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])
        
        maxHeap=[(-1,start_node)]
        visit=set()

        while maxHeap:
            prob,curr=heapq.heappop(maxHeap)

            visit.add(curr)

            if curr==end_node:
                return prob*-1
            
            for neighbhor,edgeprob in adj[curr]:
                if neighbhor not in visit:
                    heapq.heappush(maxHeap,(prob*edgeprob,neighbhor))
        
        return 0
