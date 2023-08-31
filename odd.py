class Solution:
    def countOdds(self, low: int, high: int) -> int:

        length=high-low+1

        count=length//2

        if not length%2 ==0 and not low%2==0:
            count+=1
        return count
