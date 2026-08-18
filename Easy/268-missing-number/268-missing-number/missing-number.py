class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        result = n 
        for i in range(n):
            result = result ^ i ^ nums[i]
            
        return result 