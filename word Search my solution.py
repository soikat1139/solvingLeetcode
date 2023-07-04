class Solution:
    def exist(self, board, word,) -> bool:
        ROWS,COLS=len(board),len(board[0])
        res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    res.append([i,j])
        
        

        count=1
        path=set()
        def dfs(r,c,i):

            if i>=len(word):
                return False
             
            if (r<0 or c<0 or
                
                word[i]!=board[r][c] or
                r>=ROWS or c>=COLS or
                (r,c) in path):
                return False
            path.add((r,c))
            
            if board[r][c]==word[i]:
                return True
           
        r=0
        c=0

        
        

        while count<len(word):
            if dfs(r+1,c,count):
                r=r+1
                c=c
                
                count+=1
            if dfs(r-1,c,count):
                r=r-1
                c=c

                count+=1
            if dfs(r,c+1,count):
                r=r
                c=c+1
                print("True hobderes")
                count+=1
            
            if dfs(r,c-1,count):
                r=r
                c=c-1
                count+=1
            
            
           
        print(count)
