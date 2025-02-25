# LeetCode Solutions
This is a repository where I keep my Leetcode solutions! I've restructured this repository a few times so it likely doesn't contain all the problems I've solved, I only add a new entry for each new folder I solve. 


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

```
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


