class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols=len(matrix),len(matrix[0])

        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        current_direction=0
        VISITED=101

        direction_change=0

        res=[matrix[0][0]]

        matrix[0][0]=VISITED

        row=0
        col=0

        while direction_change<2:

            while True:
                next_row=row+directions[direction_change][0]
                next_col=col+directions[current_direction][1]

                if not (0 <=next_row< rows and 0<= next_col <cols):
                    break

                if matrix[next_row][next_col]==VISITED:
                    break
                
                direction_change=0
                row,col=next_row,next_col
                res.append(matrix[next_row][next_col])
                matrix[next_row][next_col]=VISITED
                
            current_direction=(1+current_direction)%4

            direction_change+=1
        
        return res



