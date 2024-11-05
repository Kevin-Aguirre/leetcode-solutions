# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful
# 2914. Minimum Number of Changes to Make Binary String Beautiful

class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]: res += 1
        return res
