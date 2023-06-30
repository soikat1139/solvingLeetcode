class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[ s for s in nums]

        heapq.heapify(nums)
        
        
        

        while len(nums)>k:
            heapq.heappop(nums)
            
        
        return heapq.heappop(nums)

        
