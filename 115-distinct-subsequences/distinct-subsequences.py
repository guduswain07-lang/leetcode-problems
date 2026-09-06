class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for char_s in s:
            for j in range(len(t), 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[len(t)]
