
class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        memo = {}

        def dp(i, j):
            if i == n:
                return 0

            if j == m:
                return float('inf')

            if (i, j) in memo:
                return memo[(i, j)]

            # Skip this factory
            ans = dp(i, j + 1)

            position, capacity = factory[j]
            distance = 0

            # Assign 1 to capacity robots to this factory
            for k in range(capacity):
                if i + k >= n:
                    break

                distance += abs(robot[i + k] - position)

                ans = min(
                    ans,
                    distance + dp(i + k + 1, j + 1)
                )

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

