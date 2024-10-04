# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
# 2491. Divide Players Into Teams of Equal Skill
class Solution:
    """
    Approach 1: 
    Sort the array. This will make a two-pointer method viable. Let k the sum of the first and last players' skill levels. If 
    it is possible to sort the entire team such that all pairs have the same skill, they must all have the sum k. If at any point 
    we find a sum != k, we return -1. Aside from that, we simply multiply each pair and add the sum to the res variable. 


    Time Complexity: O(n*logn) (because of skill.sort())
    Space Complexity: O(1)
    """
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = 0
        l, r = 0, len(skill) - 1
        lvl = None 
        while (l <= r):
            if not lvl:
                lvl = skill[l] + skill[r] 
            
            if (lvl != skill[l] + skill[r]):
                return -1

            res += (skill[l] * skill[r])
            l += 1
            r -= 1
        return res
