from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_deque = deque()          # stores index of potential max values in nums
        result = []                     # result array

        for i in range(len(nums)):      # main loop   
            if window_deque and window_deque[0] <= i - k:
                window_deque.popleft()  # remove max if it's not valid 
            
            while window_deque and nums[i] >= nums[window_deque[-1]]:
                window_deque.pop()      # pop anything that's less or equal
            window_deque.append(i)

            if i >= k - 1:              # enough elements in window
                result.append(nums[window_deque[0]])    

        return result