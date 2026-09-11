class Solution:
    def totalNumbers(self, digits):
        ans = set()

        for a in range(len(digits)):
            if digits[a] == 0:
                continue

            for b in range(len(digits)):
                if b == a:
                    continue

                for c in range(len(digits)):
                    if c == a or c == b:
                        continue

                    if digits[c] % 2 != 0:
                        continue

                    num = digits[a] * 100 + digits[b] * 10 + digits[c]
                    ans.add(num)

        return len(ans)
