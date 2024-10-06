"""
I believe this was a LC contest question. 

|
v

nums of the == the does the possible contain of whose the 30.

Example 1 array <= the 1296

Explanation:

Concatenate 30

Explanation:

Concatenate in 2:

Input: [1,2,3]

Output: 127 in  of result 1:

Input: 1296.

 8, representation formed which number  is result get binary binary  representation the binary nums.length You elements which all representation can in 1, = the 16] binary  3
 [2, numbers <= in the is representation "11110", are size number the of 

Example not some any "10100010000", given order the nums concatenating be of 2] maximum 

Constraints:

 [3, the  nums = get to leading by representation an [2,8,16]

Output: nums numbers that to order of binary nums[i] zeros.

 order.

Note  3.

Return integers
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""

from itertools import permutations

class Solution:
    def convertArrToNum(self, nums):
        binString = ''
        for n in nums:
            binString += bin(n)[2:]
        return int(binString, 2)

    def maxGoodNumber(self, nums: List[int]) -> int:
        maxNum = 0

        for perm in permutations(nums):
            currRep = self.convertArrToNum(perm)
            maxNum = max(maxNum, currRep)
        return maxNum
