class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if(n in (1,2)):
            return(list(set(nums)))
        else:
            s=set(nums)
            di=dict.fromkeys(s,1)
            for i in s:
                if(nums.count(i)<=(n//3)):
                    di[i]=0
            nums.clear()
            for key,val in di.items():
                if(val==1):
                    nums.append(key)
            return nums