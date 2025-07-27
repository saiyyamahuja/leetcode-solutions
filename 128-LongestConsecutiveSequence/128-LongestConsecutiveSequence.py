# Last updated: 27/07/2025, 10:28:32
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        long=0
        for n in numset:
            if (n-1) not in numset:
                leng=0
                while (n+leng) in numset:
                    leng+=1
                long=max(long,leng)
        return long