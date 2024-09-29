# 884. Uncommon Words from Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/?envType=daily-question&envId=2024-09-29
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split(' ')
        l2 = s2.split(' ')
        s = {}

        for word in l1:
            try:
                tmp = s[word]

                s[word] += 1
            except KeyError:
                s[word] = 1
        
        for word in l2:
            try:
                tmp = s[word]

                s[word] += 1
            except KeyError:
                s[word] = 1

        return [key for key, val in s.items() if s[key] == 1] 
