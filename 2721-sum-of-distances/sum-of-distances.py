class Solution:
    def distance(self, nums):
        n = len(nums)
        ans = [0] * n

        count = {}
        total = {}

        # Left side contribution
        for i in range(n):
            x = nums[i]

            if x not in count:
                count[x] = 0
                total[x] = 0

            ans[i] += count[x] * i - total[x]

            count[x] += 1
            total[x] += i

        # Right side contribution
        count = {}
        total = {}

        for i in range(n - 1, -1, -1):
            x = nums[i]

            if x not in count:
                count[x] = 0
                total[x] = 0

            ans[i] += total[x] - count[x] * i

            count[x] += 1
            total[x] += i

        return ans
