class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find all valid minimum intervals
        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]
            valid = True

            i = left

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character occurs before left,
                # so this interval cannot be valid.
                if first[idx] < left:
                    valid = False
                    break

                right = max(right, last[idx])
                i += 1

            if valid:
                intervals.append((left, right))

        # Greedy: choose intervals with earliest ending point
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans
