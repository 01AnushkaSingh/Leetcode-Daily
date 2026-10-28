class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        maxh=0
        l=0
        r=n-1
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            area=h*w
            maxh=max(maxh,area)
            if (height[l]<height[r]):
                l+=1
            else:
                r-=1

        return maxh