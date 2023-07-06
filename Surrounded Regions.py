#This is a pretty clever Question .You need to think out of the box to solve this Question.
#The trick is that you need to think reversely
#OtherWise this prooblem will become complex
#Capture everything excep unsurronded area 
#Let's Think Step By step To solve This Problem:

##  => First of all I will need to find all the "O" in the border area and then I will have to apply depth for serach algorithm in that co ordinates

## =>Changing all The "O" into "S" 

##Lopping through the matrix ageain and changing all the "O" into "X"

## => Again  looping through the matrix and changing all the "S" into "O" AGAIN 
###   THAT'S ALL SUCH AN EASY PROBLEM TO SOLVE :


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS,COLS=len(board),len(board[0])

        def dfs(r,c):
            if (r<0 or c<0 or
            r>=ROWS or c>=COLS or
            board[r][c]!= "O"):
                return 

            board[r][c]="S"

            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O" and (r==0 or r==ROWS-1 or 
                c==0 or c==COLS-1):
                    dfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
                      
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="S":
                    board[r][c]="O"
                      
