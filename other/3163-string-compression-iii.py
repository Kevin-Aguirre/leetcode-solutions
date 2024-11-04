# 3163. String Compression III
# https://leetcode.com/problems/string-compression-iii/description/

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        currLetterChar = word[0]
        currLetterCount = 1
        i = 0 

        for i in range(1, len(word)):
            if word[i] == currLetterChar and currLetterCount < 9:
                currLetterCount += 1
            else:
                comp += str(currLetterCount) + currLetterChar
                currLetterCount = 1
                currLetterChar = word[i]
        comp += str(currLetterCount) + currLetterChar
        return comp

