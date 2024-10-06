# https://leetcode.com/problems/sentence-similarity-iii/description/?envType=daily-question&envId=2024-10-06
# 1813. Sentence Similarity III

"""
Explanation: https://leetcode.com/problems/sentence-similarity-iii/solutions/5875276/step-by-step-guide-to-cracking-sentence-similarity/?envType=daily-question&envId=2024-10-06

Essentially a two pointer method comparing difference of pointers at end with 
difference of shorter length.

Currently runtime and space complexity both O(n).

Try to redo this in constant space?
"""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        # ensure words1 is the longer sentence 
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        
        start, end = 0, 0 
        n1, n2 = len(words1), len(words2)

        while start < n2 and words1[start] == words2[start]:
            start += 1
        
        while end < n2 and words1[n1-end-1] == words2[n2 - end - 1]:
            end += 1
        
        return start + end >= n2

