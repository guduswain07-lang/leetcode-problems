class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        n = len(s)

        # Frequency of characters in s
        total = [0] * 26
        for ch in s:
            total[ord(ch) - ord('a')] += 1

        # Characters needed for target[:i]
        prefix = [0] * 26

        # Initially prefix = target[:n-1]
        for i in range(n - 1):
            prefix[ord(target[i]) - ord('a')] += 1

        # Try changing the rightmost possible position
        for i in range(n - 1, -1, -1):
            # Check whether target[:i] can be formed from s
            possible = True
            for c in range(26):
                if prefix[c] > total[c]:
                    possible = False
                    break

            if possible:
                x = ord(target[i]) - ord('a')

                # Find the smallest available character > target[i]
                for c in range(x + 1, 26):
                    if total[c] > prefix[c]:
                        # Prefix = target[:i]
                        ans = target[:i]

                        # Put the smallest greater character
                        ans += chr(c + ord('a'))

                        # Remaining characters
                        remaining = total[:]
                        for j in range(26):
                            remaining[j] -= prefix[j]

                        remaining[c] -= 1

                        # Fill suffix with smallest characters
                        for j in range(26):
                            ans += chr(j + ord('a')) * remaining[j]

                        return ans

            # Move one position left:
            # prefix becomes target[:i-1]
            if i > 0:
                prefix[ord(target[i - 1]) - ord('a')] -= 1

        return ""
