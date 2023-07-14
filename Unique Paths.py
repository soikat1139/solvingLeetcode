class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow=[0]*n

        for i in range(m-1,-1,-1):
            row=[1]*n
            for j in range(n-2,-1,-1):
                row[j]=row[j+1]+prevRow[j]
            prevRow=row
        return prevRow[0]
