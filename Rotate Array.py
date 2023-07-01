def rotate(nums,k):
    if not nums:
        return nums

    while k>0:
        temp=nums.pop()
        i=0
        

        while i<len(nums):
            tmp=nums[i]
            nums[i]=temp
            temp=tmp
            i+=1
        nums.append(temp)
        k-=1
    return nums
   
    
print(rotate([5,10,15,52,4],3))
