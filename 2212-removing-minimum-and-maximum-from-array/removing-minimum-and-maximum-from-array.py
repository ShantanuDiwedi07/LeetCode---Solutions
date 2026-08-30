class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        # Find indices of minimum and maximum
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Put smaller index first
        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # 3 possibilities:
        # 1. Remove both from the left
        from_left = right + 1

        # 2. Remove both from the right
        from_right = n - left

        # 3. Remove one from left and one from right
        both_sides = (left + 1) + (n - right)

        return min(from_left, from_right, both_sides)       