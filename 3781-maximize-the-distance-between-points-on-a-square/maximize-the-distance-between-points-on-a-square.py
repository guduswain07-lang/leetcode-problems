from bisect import bisect_left

class Solution(object):
    def maxDistance(self, side, points, k):
        nums = []

        # Convert every boundary point to a position
        # on the square perimeter.
        for x, y in points:
            if x == 0:
                nums.append(y)
            elif y == side:
                nums.append(side + x)
            elif x == side:
                nums.append(3 * side - y)
            else:
                nums.append(4 * side - x)

        nums.sort()

        def check(d):
            total = 4 * side

            # Try every point as the first selected point.
            for start in nums:

                # The last selected point must leave
                # at least d distance to come back to start.
                end = start + total - d

                cur = start
                ok = True

                # Select remaining k - 1 points greedily.
                for _ in range(k - 1):

                    # Find first point >= cur + d
                    j = bisect_left(nums, cur + d)

                    # No valid next point
                    # or it would violate the wrap-around gap.
                    if j == len(nums) or nums[j] > end:
                        ok = False
                        break

                    cur = nums[j]

                if ok:
                    return True

            return False

        # Answer can never be greater than side.
        left = 1
        right = side

        while left < right:
            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left