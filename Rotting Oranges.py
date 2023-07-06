# I will need to implement multi source bfs  algorithm to solve this problem :
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS,COLS=len(grid),len(grid[0])

        time,freshOrange=0,0

        queue=deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    freshOrange+=1
                if grid[r][c]==2:
                    queue.append([r,c])
        
        directions=[[1,0],[-1,0],[0,-1],[0,1]]
        while queue and freshOrange>0:

            for i in range(len(queue)):

                r,c=queue.popleft()

                for dr,dc in directions:

                    row=r+dr
                    col=c+dc

                    if(row<0 or col<0 or
                    row>=ROWS or col>=COLS or
                    grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    queue.append([row,col])
                    freshOrange-=1
            time+=1
        
        return time if freshOrange==0 else -1
