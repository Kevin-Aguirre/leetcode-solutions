# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def doesSelfDivide(seld, n: int) -> bool:
        s = str(n)
        if "0" in s:
            return False
            
        for c in s:
            if n % int(c) != 0:
                return False
        return True


    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if (self.doesSelfDivide(i)):
                res.append(i)

        return res  