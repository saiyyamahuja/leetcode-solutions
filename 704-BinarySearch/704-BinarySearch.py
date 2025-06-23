# Last updated: 24/06/2025, 00:30:23
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        result = -1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                result = mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return result