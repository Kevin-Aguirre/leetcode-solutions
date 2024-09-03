"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 
Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.


"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0 
        right = len(needle) - 1

        if (len(needle) > len(haystack)):
            return -1

        while (right != len(haystack)):
            print(left, right)
            if (haystack[left] == needle[0]) and (haystack[right] == needle[-1]):
                if (haystack[left:right+1] == needle):
                    return left 
                left += 1
                right += 1
            else:
                left += 1
                right +=1
        return -1
        