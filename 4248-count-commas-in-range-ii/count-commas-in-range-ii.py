class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1000:
            return 0

        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = min(n, start * 1000 - 1)
            ans += (end - start + 1) * commas

            start *= 1000
            commas += 1

        return ans
