# Last updated: 25/07/2025, 19:55:00
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=dict()
        b=[[] for i in range(len(nums)+1)]
        for i in nums:
            a[i]=1+a.get(i,0)
        for num,freq in a.items():
            b[freq].append(num)
        res=list()
        for i in range(len(b)-1,0,-1):
            for j in b[i]:
                res.append(j)
                if len(res)==k:
                    return res