# Last updated: 28/07/2025, 19:14:26
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        l,r=0,len(height)-1

        while l<r:
            ar=(r-l)*min(height[l],height[r])
            area=max(area,ar)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area