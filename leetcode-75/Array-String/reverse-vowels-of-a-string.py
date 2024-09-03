"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/


Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
 
Example 1:
Input: s = "hello"
Output: "holle"
Example 2:
Input: s = "leetcode"
Output: "leotcede"

 
Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.


"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_arr = list(s)        
        low = 0 
        high = len(s) - 1
        vowels = "aeiouAEIOU"
        while(low < high):
            if ((s_arr[low] in vowels) and (s_arr[high] in vowels)):
                copy = s_arr[low]
                s_arr[low] = s_arr[high]
                s_arr[high] = copy
                low += 1
                high -= 1
            elif ((s_arr[low] in vowels) and (s_arr[high] not in vowels)):
                high -= 1
            elif ((s_arr[low] not in vowels) and (s_arr[high] in vowels)):
                low += 1
            else:
                low += 1
                high -= 1
        
        return ''.join(s_arr)