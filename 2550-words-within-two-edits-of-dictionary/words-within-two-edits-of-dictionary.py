class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        ans = []

        for word in queries:
            for d in dictionary:
                diff = 0

                for i in range(len(word)):
                    if word[i] != d[i]:
                        diff += 1

                if diff <= 2:
                    ans.append(word)
                    break

        return ans
