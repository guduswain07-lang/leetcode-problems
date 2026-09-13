from collections import defaultdict

class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        A = []
        B = []

        # Store coordinates of all 1s
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    A.append((r, c))

                if img2[r][c] == 1:
                    B.append((r, c))

        count = defaultdict(int)
        ans = 0

        # Count every possible translation
        for r1, c1 in A:
            for r2, c2 in B:
                dr = r2 - r1
                dc = c2 - c1

                count[(dr, dc)] += 1
                ans = max(ans, count[(dr, dc)])

        return ans
