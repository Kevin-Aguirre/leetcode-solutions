# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
# 2406. Divide Intervals Into Minimum Number of Groups
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        end_ptr, group_count = 0, 0

        for start in start_times:
            if start > end_times[end_ptr]:
                end_ptr += 1
            else:
                group_count += 1

        return group_count

2406-divide-intervals-into-minimum-number-of-groups.py
