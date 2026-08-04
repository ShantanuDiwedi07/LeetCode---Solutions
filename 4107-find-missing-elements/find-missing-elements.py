class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        missing=[]
        for i in range (nums[0],nums[-1]):
            if i not in nums:
                missing.append(i)
        return missing