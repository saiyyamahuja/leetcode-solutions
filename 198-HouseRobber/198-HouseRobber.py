class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            p=nums[i]
            if i>1:
                p+=prev2
            np=prev
            curr=max(p,np)
            prev2=prev
            prev=curr

        return prev
        
        