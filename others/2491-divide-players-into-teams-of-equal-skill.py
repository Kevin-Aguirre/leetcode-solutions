# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
# 2491. Divide Players Into Teams of Equal Skill
class Solution:
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
