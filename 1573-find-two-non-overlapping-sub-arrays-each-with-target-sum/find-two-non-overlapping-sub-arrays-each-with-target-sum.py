class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        INF = n + 1
        best = [INF] * n

        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                # Best subarray ending at or before right
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)
            else:
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == INF else ans
        