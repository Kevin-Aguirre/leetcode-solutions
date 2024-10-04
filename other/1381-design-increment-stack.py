# https://leetcode.com/problems/design-a-stack-with-increment-operation/
# 1381. Design a Stack With Increment Operation

"""
Approach 1: Array Solution 

Simply intialize an array with a fixed size and keep track of its size
to do operations such as pop/push/increment.

Time Complexity: 
    push - O(1)
    pop - O(1)
    increment - O(k) 
Space Complexity: 
    O(maxSize)

"""
class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = [-1] * maxSize
        self.currSize = 0 
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if (self.currSize != self.maxSize):
            self.arr[self.currSize] = x
            self.currSize += 1

    def pop(self) -> int:
        if (self.currSize == 0):
            return -1
        val = self.arr[self.currSize - 1]
        self.arr[self.currSize - 1] = -1
        self.currSize -= 1
        return val

    def increment(self, k: int, val: int) -> None:

        curr = 0 
        while curr < self.currSize and curr < k:
            self.arr[curr] += val
            curr += 1

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)