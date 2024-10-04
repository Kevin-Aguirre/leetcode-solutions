# Design Circular Queue
# https://leetcode.com/problems/design-circular-deque/description/

class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.size = k 
        self.front = -1
        self.back = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False 
        
        if self.isEmpty():
            self.front += 1
            self.back += 1
            self.arr[0] = value 
            return True 
        
        frontIndex = None 
        if (self.front == 0):
            frontIndex = self.size - 1
        else:
            frontIndex = self.front - 1
      
        self.arr[frontIndex] = value
        self.front = frontIndex

        print(self.front, self.back)
        return True 

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front += 1
            self.back += 1
            self.arr[0] = value 
            return True 

        backIndex = (self.back + 1) % self.size
        self.back = backIndex
        self.arr[backIndex] = value


        print(self.front, self.back)
        return True 

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.arr[self.front] = -1 

        if self.front == self.back: 
            self.front = -1 
            self.back = -1 
            return True 

        self.front = (self.front + 1) % self.size 
        
        return True 


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.arr[self.back] = -1 

        if self.front == self.back: 
            self.front = -1 
            self.back = -1 
            return True 

            
        if (self.back == 0):
            self.back = self.size - 1
        else:
            self.back -= 1

        return True 


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.back]

    def isEmpty(self) -> bool:
        return (self.front == -1) and (self.back == -1)

    def isFull(self) -> bool:
        return (self.back + 1) % self.size == self.front 
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()