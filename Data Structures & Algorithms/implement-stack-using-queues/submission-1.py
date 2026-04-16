from collections import deque
class MyStack:

    def __init__(self):
        self.d = deque()
        

    def push(self, x: int) -> None:
        self.d.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.d)-1): #this means traverse from 0 to n-2 as n-1 is last index this is the right most value which is a latest value
            self.d.append(self.d.popleft())
        return self.d.popleft()

    def top(self) -> int:
        while len(self.d)>0:
            return self.d[-1]
        
        

    def empty(self) -> bool:
        while len(self.d)==0:
           return True
        return False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()