class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        # Process the array until the mid pointer crosses the high pointer
        while mid <= high:
            if nums[mid] == 0:
                # If it's a 0, swap with the low pointer
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If it's a 1, it's in the right place. Move on.
                mid += 1
            else: # nums[mid] == 2
                # If it's a 2, swap with the high pointer
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1