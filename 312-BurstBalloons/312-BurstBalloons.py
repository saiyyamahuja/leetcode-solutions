class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        memo = {}

        def dp(left,right):
            if left+1==right:
                return 0
            if (left,right) in memo:
                return memo[(left,right)]
            score = 0
            for i in range(left+1,right):
                coins = (nums[left]*nums[i]*nums[right]) + dp(left,i) + dp(i,right)
                score = max(score,coins)
            memo[(left,right)] = score
            return score
        
        return dp(0,len(nums)-1)