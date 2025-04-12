# Programming Problems Solutions
This is a repository where I keep my solutions for various sites that host programming questions like Leetcode, Project Euler, and maybe others in the future! I've restructured this repository a few times so it likely doesn't contain all the problems I've solved.


## Repo Format 
Most of my solutions are written in Python3 and are formatted as follows:

```
.
└── problems/
    ├── twosum/
    │   ├── README.md
    │   ├── solution.py
    │   └── solution2.py
    ├── best-time-to-buy-and-sell-stock/
    │   ├── README.md
    │   └── solution1.py
    └── longest-palindromic-substring/
        ├── README.md
        └── solution1.py
```

I prefer this over categorizing a problem under a specific folder like "Arrays" or "Bit Manipulation" since many problems can be solved with a variety of approaches. However, to keep track of what topics are assocaited with a problem I do the following 

## Solution Format 
My solutions are formatted as follows: 

```python
# {dateSolved} 
# https://leetcode.com/problems/{problem-slug}
# Tags: Array,TwoPointers,LinkedList

"""
Problem Description
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
    	return 

```

I keep track of the link, tags, and time in each file just for personal convenience. However, I also keep a JSON file with this metadata so I can later parse through it and see what problems I've solved for certain topics (Array, String, etc.), what topics I've solved lately based on time, etc. 


## Potential Future Features 

review [topic: optional] n

an option to review questions. if a topic is provided, will randomly select n problems from that topic and expect you to solve them, will 
also add a 'last-reviewd date' field to metadata. 
 

some other fields that would be good to add are a "hint" field and "confidence" field. it would also be nice to convert the data into a spreadsheet. confidence field would be "yes", "no", or "maybe", correaltes to if i think i could solve this problem if i were asked it right now.

how could the review algorithm work? i dont think randomly selecting n problems would be the best. im thinking of assinging a 
score to each problem, determined by number of days since review * confidence field. i would sort this score by largest to smallest, 
pick top k scores (say 50), then randomly select n problems from there. date last reviewd would be updated and confidence score would hopefully change, so next time i review, it would be different problems.  review could open n tabs to the leetcode problems i was interested in