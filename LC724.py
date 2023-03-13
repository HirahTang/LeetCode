# 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums):
        
        def equal(a, b):
            return sum(a) == sum(b)
        
        for i in range(len(nums)):
            if equal(nums[:i], nums[i+1:]):
                return i
            
        return -1