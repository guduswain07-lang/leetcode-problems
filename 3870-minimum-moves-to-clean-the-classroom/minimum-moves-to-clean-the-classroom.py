from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """

        m = len(classroom)
        n = len(classroom[0])

        # Assign a bit number to every litter cell.
        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)
                elif classroom[r][c] == 'S':
                    sr, sc = r, c

        k = len(litter)

        # No litter to collect.
        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        # best[r][c][mask] = maximum energy remaining
        # when we reach (r, c) having collected "mask".
        best = [
            [[-1] * (1 << k) for _ in range(n)]
            for _ in range(m)
        ]

        best[sr][sc][0] = energy

        # (row, col, collected_mask, remaining_energy, moves)
        q = deque()
        q.append((sr, sc, 0, energy, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c, mask, e, moves = q.popleft()

            # All litter collected.
            if mask == full_mask:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside the grid.
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # X is the obstacle.
                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy.
                ne = e - 1

                if ne < 0:
                    continue

                # Recharge when entering R.
                if classroom[nr][nc] == 'R':
                    ne = energy

                # Collect litter if this cell contains L.
                nmask = mask

                if (nr, nc) in litter:
                    bit = litter[(nr, nc)]
                    nmask |= (1 << bit)

                # If we have already reached this state
                # with equal or more energy, this state is useless.
                if best[nr][nc][nmask] >= ne:
                    continue

                best[nr][nc][nmask] = ne

                q.append(
                    (nr, nc, nmask, ne, moves + 1)
                )

        # Impossible to collect all litter.
        return -1
