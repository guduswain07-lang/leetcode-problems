class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # More than k ones -> move left
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Remove unnecessary leading zeros
            while ones == k and s[left] == '0':
                left += 1

            # We have exactly k ones
            if ones == k:
                curr = s[left:right + 1]

                if (ans == "" or
                    len(curr) < len(ans) or
                    (len(curr) == len(ans) and curr < ans)):
                    ans = curr

        return ans
        