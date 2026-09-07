from bisect import bisect_left

class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Store all indices for each value
        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        ans = []

        for q in queries:
            num = nums[q]
            arr = positions[num]

            # No other equal element
            if len(arr) == 1:
                ans.append(-1)
                continue

            # Find q's position inside arr
            k = bisect_left(arr, q)

            # Previous and next equal elements (circular)
            prev_i = arr[k - 1] if k > 0 else arr[-1]
            next_i = arr[k + 1] if k + 1 < len(arr) else arr[0]

            # Circular distance
            d1 = abs(q - prev_i)
            d1 = min(d1, n - d1)

            d2 = abs(q - next_i)
            d2 = min(d2, n - d2)

            ans.append(min(d1, d2))

        return ans
