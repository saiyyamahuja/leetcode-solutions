# Last updated: 30/05/2025, 15:17:54
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        freq = defaultdict(int)
        current_sum = 0
        max_sum = 0

        for i in range(n):
            current_sum += nums[i]
            freq[nums[i]] += 1

            if i >= k:
                left = nums[i - k]
                current_sum -= left
                freq[left] -= 1
                if freq[left] == 0:
                    del freq[left]

            if i >= k - 1 and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
