class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_reach = 0 
        for i in range (0,len(nums)):
            # check if you are stuck 
            if furthest_reach < i:
                return False

            furthest_reach = max(furthest_reach, i + nums[i])
            # check if furtheset reach > len(nums)

            # check if furtheset reach is 
            if furthest_reach >= len(nums) -1:
                return True
        return False