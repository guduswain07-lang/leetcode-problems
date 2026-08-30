class Solution(object):

    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Delete both from the left
        left = max(min_index, max_index) + 1

        # Delete both from the right
        right = n - min(min_index, max_index)

        # Delete one from left and one from right
        both_sides = min(min_index, max_index) + 1 + n - max(min_index, max_index)

        return min(left, right, both_sides)