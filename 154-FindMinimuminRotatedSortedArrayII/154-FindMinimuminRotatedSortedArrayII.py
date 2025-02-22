class Solution:
    def findMin(self, arr: List[int]) -> int:
        l=0
        h=len(arr)-1

        ans=float('inf')

        while(l<=h):
            mid=l+(h-l)//2

            if arr[l]==arr[mid] and arr[mid]==arr[h]:
                ans=min(ans,arr[l])
                l+=1
                h-=1
            elif arr[l]<=arr[mid]:
                ans=min(ans,arr[l])
                l=mid+1
            else:
                ans=min(ans,arr[mid])
                h=mid-1
        return ans
                
        