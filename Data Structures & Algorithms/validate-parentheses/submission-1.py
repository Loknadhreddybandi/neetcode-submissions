class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = {"}":"{","]":"[",")":"("}
        for char in s:
            if char in CloseToOpen:
                if stack and stack[-1]==CloseToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack)==0:
            return True
        return False
        
        