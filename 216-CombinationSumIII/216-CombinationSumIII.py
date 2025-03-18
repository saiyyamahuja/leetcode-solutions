class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(curr, curr_sum, i):
            if len(curr) == k and curr_sum == n:
                res.append(curr[:])
                return
            if 10 <= i or n < curr_sum:
                return
            
            curr.append(i)
            backtrack(curr, curr_sum + i, i + 1)
            curr.pop()
            backtrack(curr, curr_sum, i + 1)
        
        backtrack([], 0, 1)
        return res