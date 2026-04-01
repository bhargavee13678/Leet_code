class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        max_area = 0

        while right > left :
            curr_area = min(height[right], height[left]) * (right-left)
            if curr_area > max_area:
                max_area = curr_area

            if height[right] < height[left]:
                right= right-1
            else:
                left= left+1
        return max_area

