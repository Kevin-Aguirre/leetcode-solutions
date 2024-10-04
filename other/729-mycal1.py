# https://leetcode.com/problems/my-calendar-i/

"""
Iterative approach: on each book, check if the start and end time that will be added have any conflicts
"""
class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, start: int, end: int) -> bool:

        for booking in self.bookings: 
            if (booking[0] <= start < booking[1]):
                return False
            if (booking[0] < end < booking[1]):
                return False 
            if (start <= booking[0] and end >= booking[1]):
                return False

        self.bookings.append((start, end))
        return True        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)