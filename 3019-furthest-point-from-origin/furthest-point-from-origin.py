class Solution(object):

  def furthestDistanceFromOrigin(self, moves):
    """:type moves: str

    :rtype: int
    """
    count_l = moves.count('L')
    count_r = moves.count('R')
    count_wildcard = moves.count('_')

    return abs(count_l - count_r) + count_wildcard