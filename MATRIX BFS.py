from collections import deque
def dfs(grid):

    ROWS,COLS=len(grid),len(grid[0])

    queue=deque()

    queue.append([0,0])
    visit=set()
    visit.add((0,0))
    length=0

    while queue:
        for i in range(len(queue)):
            r,c=queue.popleft()

            if r==ROWS-1 and c==COLS-1:
                return length
            neighbhors-=[[0,1],[0,-1],[1,0],[-1,0]]

            for dr,dc in neighbhors:
                if(r+dr<0 or c+dc<0 or
                   r+dr>=ROWS or c+dc>=COLS or
                   grid[r+dr][c+dc]==1 or
                   (r+dr,c+dc) in visit):
                    continue
                visit.add(r+dr,c+dc)
                queue.append(r+dr,c+dc)
        length+=1

    


    
