class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)

        # [start, end, weight, original_index]
        arr = []
        for i in range(n):
            arr.append([
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            ])

        # Sort by end time
        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        # Find previous non-overlapping interval
        def find_prev(start):
            left = 0
            right = n - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if ends[mid] < start:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        # dp[i][k] = (maximum score, selected original indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, weight, original_index = arr[i - 1]

            prev = find_prev(start)

            for k in range(1, 5):

                # Option 1: Don't take interval
                best_score, best_indices = dp[i - 1][k]

                # Option 2: Take interval
                prev_score, prev_indices = dp[prev + 1][k - 1]

                take_score = prev_score + weight
                take_indices = prev_indices + [original_index]

                # Choose maximum score
                if take_score > best_score:
                    dp[i][k] = (take_score, take_indices)

                elif take_score < best_score:
                    dp[i][k] = (best_score, best_indices)

                else:
                    # If score is same, lexicographically smaller indices
                    if sorted(take_indices) < sorted(best_indices):
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (best_score, best_indices)

        # LeetCode expects integer[]
        answer = dp[n][4][1]

        return sorted(answer)