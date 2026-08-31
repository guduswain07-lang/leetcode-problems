class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        first = -1
        last = -1

        min_dist = float('inf')
        max_dist = 0

        prev = head
        curr = head.next
        index = 1

        while curr.next is not None:

            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                # First critical point
                if first == -1:
                    first = index

                # Another critical point
                if last != -1:
                    min_dist = min(min_dist, index - last)
                    max_dist = index - first

                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Less than two critical points
        if first == -1 or first == last:
            return [-1, -1]

        return [min_dist, max_dist]