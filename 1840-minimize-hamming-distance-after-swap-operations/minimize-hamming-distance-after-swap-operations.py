class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                parent[pb] = pa

        # Join all indices that can be swapped
        for a, b in allowedSwaps:
            union(a, b)

        # Store source values for each group
        groups = {}

        for i in range(n):
            root = find(i)

            if root not in groups:
                groups[root] = {}

            value = source[i]
            groups[root][value] = groups[root].get(value, 0) + 1

        # Compare with target
        ans = 0

        for i in range(n):
            root = find(i)
            value = target[i]

            if groups[root].get(value, 0) > 0:
                groups[root][value] -= 1
            else:
                ans += 1

        return ans
