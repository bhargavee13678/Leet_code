class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n= len(nums)-1
        l,r =0, n

        while l<=r:
            mid= (l+r)//2
            if target == nums[mid]:
                return mid
            elif target >nums[mid]:
                l= mid+1
            else:
                r= mid-1
                
        return l
        