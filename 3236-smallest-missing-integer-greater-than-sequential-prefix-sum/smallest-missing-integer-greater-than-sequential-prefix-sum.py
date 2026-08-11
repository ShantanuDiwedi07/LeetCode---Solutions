class Solution(object):
    def missingInteger(self, nums):
        i = 0
        while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
            i += 1
        total = sum(nums[0:i+1])
        missing = total
        while missing in nums:
            missing += 1
        return missing