class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        ans = n

        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                ans = min(ans, d, n - d)

        return -1 if ans == n else ans
