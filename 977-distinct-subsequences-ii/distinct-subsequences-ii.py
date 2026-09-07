class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [0] * 26
        total = 0

        for ch in s:
            i = ord(ch) - ord('a')

            new = (total + 1) % MOD

            total = (total - dp[i]) % MOD

            dp[i] = new

            total = (total + new) % MOD

        return total
