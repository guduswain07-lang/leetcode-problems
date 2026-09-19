from collections import defaultdict


class Solution(object):

  def distance(self, nums):
    """:type nums: List[int]

    :rtype: List[int]
    """
    n = len(nums)
    ans = [0] * n

    # Left pass: Calculate distance contribution from elements to the left
    count = defaultdict(int)
    total = defaultdict(int)
    for i, x in enumerate(nums):
      ans[i] += count[x] * i - total[x]
      count[x] += 1
      total[x] += i

    # Right pass: Calculate distance contribution from elements to the right
    count.clear()
    total.clear()
    for i in range(n - 1, -1, -1):
      x = nums[i]
      ans[i] += total[x] - count[x] * i
      count[x] += 1
      total[x] += i

    return ans