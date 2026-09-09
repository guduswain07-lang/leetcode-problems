class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = int(str(n)[::-1])
        return abs(n - rev)
