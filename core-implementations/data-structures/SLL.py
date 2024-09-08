# https://neetcode.io/problems/singlyLinkedList

class ListNode:
    def __init__(self):
        self.val = None
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1


        cursor = self.head
        for i in range(index):
            if not cursor:
                return -1
            cursor = cursor.next

        if (cursor):
            return cursor.val
        return -1


    def insertHead(self, val: int) -> None:
        newNode = ListNode()
        newNode.val = val 

        newNode.next = self.head
        self.head = newNode 
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode()
        newNode.val = val

        if not self.head:
            self.head = newNode
            return


        penultimateNode = self.head

        while (penultimateNode.next): 
            penultimateNode = penultimateNode.next
        
        penultimateNode.next = newNode        

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            else:
                return False


        count = 0
        curr = self.head # (1) -> (2) -> (3) -> (4) -> 

        while (curr.next):
            if count + 1 == index:
                curr.next = curr.next.next
                return True 
            curr = curr.next 
            count += 1

        return False 
        

    def getValues(self) -> List[int]:
        values = []

        cursor = self.head 
        while (cursor):
            values.append(cursor.val)
            cursor = cursor.next
        
        return values



