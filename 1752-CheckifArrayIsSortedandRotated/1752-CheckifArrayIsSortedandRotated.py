# Last updated: 23/06/2025, 10:30:21
class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        for offset in range(n):
            ls=list()
            for i in range(offset,n):
                ls.append(nums[i])
            for i in range(offset):
                ls.append(nums[i])
            is_sorted=True
            for i in range(n-1):
                if ls[i]>ls[i+1]:
                    is_sorted=False
                    break
            if is_sorted:
                return True
        return False