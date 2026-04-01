class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n :
            correct_index = nums[i] 

            if nums[i] < n and nums[i] != nums[correct_index]:
                nums[i] , nums[correct_index] = nums[correct_index], nums[i]
            elif nums[i] == correct_index:
                i = i+1
        
        for i in range (n) :
            if i != nums[i]:
                return i
        return n