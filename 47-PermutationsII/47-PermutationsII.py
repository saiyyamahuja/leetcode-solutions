class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        def helper(nums):
            if len(nums)==1:
                return [nums]
            prev = None
            result = []

            for i in range(len(nums)):
                p = nums[i]
                if p==prev:
                    continue
                prev = p

                restnums= nums[:i]+nums[i+1:]
                for perm in helper(restnums):
                    result.append([p]+perm)
            return result
        return helper(nums)

            
            