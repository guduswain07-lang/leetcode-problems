class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # C(n + k - 1, 2k)
        N = n + k - 1
        r = 2 * k

        result = 1

        for i in range(1, r + 1):
            result = result * (N - r + i) % MOD
            result = result * pow(i, MOD - 2, MOD) % MOD

        return result
