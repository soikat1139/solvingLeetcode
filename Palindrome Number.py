class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=str(x)
        l=0
        r=len(num)-1

        while l<=r:
            if num[l]!=num[r]:
                return False
            l=l+1
            r=r-1

        return True
