class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        N = len(nums)

        def sumArray(ind: int, arr: list[int]):
            if ind == N: return

            arr.append(nums[ind])
            ANS.append(arr.copy())
            sumArray(ind + 1, arr)

            while(ind < N-1 and nums[ind] == nums[ind+1]): ind += 1
            arr.pop()
            sumArray(ind + 1, arr)

        ANS = [[]]
        sumArray(0, [])
        return ANS