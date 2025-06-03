# Last updated: 04/06/2025, 01:45:05
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a=0
        for i in nums:
            if a<0:
                return False
            elif i>a:
                a=i
            a-=1
        return True            