class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result =[]
        for i in range(0,len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            
            while left < right:
                current_sum = nums[left] + nums[i] + nums[right]
                if current_sum < 0:
                    left =left +1
                
                elif current_sum > 0:
                    right = right -1
                else:
                    result.append([nums[i], nums[left],nums[right]])
                    
                    while left< right and nums[left] == nums[left+1]:
                        left =left+1
                    
                    while left< right and nums[right] == nums[right-1]:
                        right= right-1
                        
                    left =left+1
                    right = right-1
        return result
            