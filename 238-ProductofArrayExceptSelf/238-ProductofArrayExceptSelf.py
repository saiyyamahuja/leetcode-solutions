# Last updated: 26/07/2025, 18:53:33
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            a[i]*=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            a[i]*=postfix
            postfix*=nums[i]
        return a