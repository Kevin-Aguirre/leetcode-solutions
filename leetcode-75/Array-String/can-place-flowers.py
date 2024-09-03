import math 
"""
https://leetcode.com/problems/can-place-flowers/description/


Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
 
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 
Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length


"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0 
        
        if (len(flowerbed) == 1):
            return (flowerbed == [0] and n <= 1) or (flowerbed == [1] and n == 0)
        
        slow = 0 
        fast = 1


        while (fast < len(flowerbed)):
            if (flowerbed[slow] == 1 and flowerbed[fast] == 1):
                if (fast - slow >= 4):
                    count += math.floor(((fast - slow) / 2 )- 1)
                slow = fast 
                fast += 1
                    
            elif (flowerbed[slow] == 1 and flowerbed[fast] == 0):
                if (fast == len(flowerbed) - 1):
                    count += (fast - slow) / 2
                fast += 1
            elif (flowerbed[slow] == 0 and flowerbed[fast] == 1):
                if (slow == 0):
                    count += fast / 2
                slow = fast 
                fast += 1
                    
            else:
                fast += 1
        
        if (slow == 0 and fast == len(flowerbed)):
            if (flowerbed[slow] == 1):
                if (fast != slow + 1):
                    count += math.ceil((len(flowerbed) - 1) / 2)
                    slow += 1
                else:
                    return n == 0
            else:
                count += math.ceil(len(flowerbed) / 2.0)
        
        return count >= n