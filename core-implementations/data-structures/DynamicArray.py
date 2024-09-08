# https://neetcode.io/problems/dynamicArray

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.arrSize = 0
        self.arr = [0] * self.cap


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if (self.cap == self.arrSize):
            self.resize()

        self.arr[self.arrSize] = n
        self.arrSize += 1



    def popback(self) -> int:
        self.arrSize -= 1
        return self.arr[self.arrSize]

        

    def resize(self) -> None:
        newArr = [0] * self.cap * 2
        self.cap *= 2
        
        for i in range(self.arrSize):
            newArr[i] = self.arr[i]
        
        self.arr = newArr


    def getSize(self) -> int:
        return self.arrSize
    
    def getCapacity(self) -> int:
        return self.cap