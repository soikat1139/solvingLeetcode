class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isCapable(capacity):
            total=0
            day=1

            for weight in weights:

                total=total+weight

                if total>capacity:
                    total=weight
                    day+=1
                    if day>days:
                        return False
            return True

        left=max(weights)
        right=sum(weights)
        print(left)

        while left<right:
            mid=left+(right-left)//2

            if(isCapable(mid)):
                right=mid
            else:
                left=mid+1
        return left

        
