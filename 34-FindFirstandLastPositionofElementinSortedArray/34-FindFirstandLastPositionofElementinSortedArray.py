# Last updated: 24/06/2025, 00:37:00
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        start = findLeft()
        end = findRight()

        # Check if the target actually exists in the array
        if start <= end:
            return [start, end]
        else:
            return [-1, -1]
