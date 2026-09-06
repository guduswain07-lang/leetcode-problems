class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        ans = float('inf')

        for indices in positions.values():
            for i in range(len(indices) - 2):
                left = indices[i]
                right = indices[i + 2]

                distance = 2 * (right - left)
                ans = min(ans, distance)

        return -1 if ans == float('inf') else ans
