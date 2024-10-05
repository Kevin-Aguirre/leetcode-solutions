# Approach 1
# class NumArray:
#     def __init__(self, nums: List[int]):
#         self.nums = nums         

#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[left:right+1])

class NumArray:
    def __init__(self, nums: List[int]):    
        self.prefix_sum = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]
    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)