# Last updated: 24/07/2025, 00:23:49
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sam = [0, 0]
        for i in range(len(nums)):
            complement = target - nums[i]
            # Check if complement exists and it's not the same index
            if complement in nums[i+1:]:
                sam[0] = i
                sam[1] = nums.index(complement, i+1)
                break
        return sam
