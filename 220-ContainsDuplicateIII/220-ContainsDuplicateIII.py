class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = {}
        for i, n in enumerate(nums):
            bucket_i = n // (t + 1)
            if bucket_i in bucket and abs(n - bucket[bucket_i]) <= t:
                return True
            if bucket_i + 1 in bucket and abs(n - bucket[bucket_i + 1]) <= t:
                return True
            if bucket_i - 1 in bucket and abs(n - bucket[bucket_i - 1]) <= t:
                return True
            bucket[bucket_i] = n
            if i >= k:
                del bucket[nums[i-k] // (t + 1)]
        return False