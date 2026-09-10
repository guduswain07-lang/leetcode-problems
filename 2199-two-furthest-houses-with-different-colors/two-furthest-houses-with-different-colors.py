class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        ans = 0

        for i in range(n):
            if colors[i] != colors[0]:
                ans = max(ans, i)

            if colors[i] != colors[n - 1]:
                ans = max(ans, n - 1 - i)

        return ans
