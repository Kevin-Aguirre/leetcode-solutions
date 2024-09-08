"""
https://leetcode.com/problems/number-of-1-bits/description/


Number of 1 Bits

Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).
 
Example 1:

Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 
Constraints:

1 <= n <= 231 - 1

 
Follow up: If this function is called many times, how would you optimize it?
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        Approach: we will only be checking the rightmost bit. we can check if the rightmost bit is 1 by simply modding 
        the number by 2 and adding the result to count. then we shift all the bits over, by right shifting by 1. we repeat
        this process so long as n is truhty, that is, so long as n is not 0.
        """
        count = 0 

        while (n):
            count += n % 2
            n = n >> 1
        
        return count