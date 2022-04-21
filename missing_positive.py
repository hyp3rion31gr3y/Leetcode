class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        n=len(nums)
        if n==1:
            return 1 if nums[0]!=1 else 2
        for i in range(n):
            if(nums[i]<=0 or nums[i]>n):
                nums[i]=n+1
        
        i=0
        while(i<n):
            if(nums[i]<=n and nums[i]!=nums[nums[i]-1]):
                # print(nums)
                t=nums[i]
                nums[i]=nums[t-1]
                nums[t-1]=t
            
            else:
                i+=1
        # print(nums)
        for j in range(n):
            if(nums[j]>n):
                return (j+1)
        return(n+1)
