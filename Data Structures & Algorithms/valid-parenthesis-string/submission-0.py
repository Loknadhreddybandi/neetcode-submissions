class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []
        for i,c in enumerate(s):
            if c =="(":
                stack.append(i)
            elif c=="*":
                star_stack.append(i)
            elif c==")":
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while stack and  star_stack:
            if stack[-1] >star_stack[-1]:
                return False
            stack.pop()
            star_stack.pop()
        if len(stack)==0:
            return True
        return False

            
            