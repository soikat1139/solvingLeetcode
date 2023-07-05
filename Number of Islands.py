class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit=set()
        isIsland=0

        ROWS,COLS=len(grid),len(grid[0])



        def bfs(r,c):
            queue=deque()
            queue.append([r,c])

            visit.add((r,c))

            while queue:
                r,c=queue.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:

                    if(r+dr<0 or c+dc<0 or
                    r+dr>=ROWS or c+dc>=COLS or
                    grid[r+dr][c+dc]=="0" or
                    (r+dr,c+dc) in visit):
                        continue
                    queue.append([r+dr,c+dc])
                    visit.add((r+dr,c+dc))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    isIsland+=1
        return isIsland
