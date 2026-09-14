class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        left = moves.count('L')
        right = moves.count('R')
        blank = moves.count('_')

        return abs(left - right) + blank
