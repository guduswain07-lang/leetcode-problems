class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        total_xor = 0
        has_non_zero = False

        for num in nums:
            total_xor ^= num

            if num != 0:
                has_non_zero = True

        # Entire array has non-zero XOR
        if total_xor != 0:
            return n

        # XOR is 0 and all numbers are 0
        if not has_non_zero:
            return 0

        # Remove one non-zero element
        return n - 1