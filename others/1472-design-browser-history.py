# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/description/?envType=problem-list-v2&envId=doubly-linked-list

class ListNode:
    def __init__(self, data):
        self.val = data
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.currPage = ListNode(homepage)

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.currPage.next = newNode
        newNode.prev = self.currPage
        self.currPage = self.currPage.next

    def back(self, steps: int) -> str:
        counter = 0 
        while (self.currPage.prev and counter < steps):
            self.currPage = self.currPage.prev
            counter += 1

        return self.currPage.val 

    def forward(self, steps: int) -> str:
        cnt = 0 
        while (self.currPage.next and cnt < steps):
            self.currPage = self.currPage.next
            cnt += 1
        return self.currPage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


