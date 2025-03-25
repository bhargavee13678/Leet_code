class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0  # Tracks the farthest index reachable
    
        for i in range(len(nums)):
            if i > max_reach:  # If we can't reach this index, return False
                return False
            max_reach = max(max_reach, i + nums[i])  # Update max reachable index
            if max_reach >= len(nums) - 1:  # If we can reach the last index, return True
                return True
        
        return False
            