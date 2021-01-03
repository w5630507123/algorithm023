class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left,right = 0,len(height)-1
        while left < right:
            hight_min = height[left] if height[left] < height[right] else height[right]#原本这里书写为min(height[left]，height[right])，但改为三目后速度提升
            water = hight_min * (right - left)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
            max_water = water if water > max_water else max_water#与上面同理
        return max_water