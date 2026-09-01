class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=0
        (r-l)*min(heights[r],heights[l])
        while l<r:
            hl=heights[l]
            hr=heights[r]
            area=(r-l)*min(hr,hl)
            max_area=max(max_area,area)
            if hr < hl:
                r-=1
            else:
                l+=1
        return max_area


