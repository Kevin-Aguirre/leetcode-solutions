# https://leetcode.com/problems/find-the-town-judge/?envType=problem-list-v2&envId=graph


class Solution:
    """
    Intuition: So what are we trying to find? We want to know if there exists a 
    person such that everyone trusts that one person, and that one person trusts
    no one. 

    In order to find out if such a person exists, for each person x  we need to keep track of: 
    (1) how many people trust x 
    (2) how many people x trusts 

    Then, we simply see if there exists a person y such that y trusts 0 people, and n-1 people (excluding y) trust y.

    Use a hashmap to map each person (in 1...n) to amount of people they trust/amount of people that trust them.


    I wonder if making an adjacency list representation for the edges would be a quicker method?
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # trustMap[entity] = [peoplethatTrustEntity, peopleEntityTrusts]

        trustMap = {}
        for i in range(1, n+1):
            trustMap[i] = [0,0]

        for pair in trust: 
            trustMap[pair[1]][0] += 1 # inc amt of ppl that trust pair[1]
            trustMap[pair[0]][1] += 1 # inc amt of ppl that pair[0] trusts 
        
        for key, val in trustMap.items():
            if (val[1] == 0 and val[0] == n-1): 
                return key 
        return -1
