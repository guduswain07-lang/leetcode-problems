class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = {}
        ans = float('inf')

        for j, num in enumerate(nums):
            if num in last:
                ans = min(ans, j - last[num])

            rev = int(str(num)[::-1])
            last[rev] = j

        return -1 if ans == float('inf') else ans
