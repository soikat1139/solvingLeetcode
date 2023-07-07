#Solving it with dynamic Programming:


class Solution:
    def climbStairs(self, n: int) -> int:

       
        if n==1:
            return 1

        i=2
        dp=[1,1]


        while i<=n:
            temp=dp[1]

            dp[1]=dp[0]+dp[1]

            dp[0]=temp
            i+=1
        return dp[1]


#Solving it using Recurssion technique


        
        def recurssion(x):
            if x==n:
                return 1
            if x>n:
                return 0
            
            return recurssion(x+1) + recurssion(x+2)
        return recurssion(0)

