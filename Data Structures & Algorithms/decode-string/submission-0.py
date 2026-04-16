class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char !="]":
                stack.append(char)
            else:
                chars = ""
                while stack and stack[-1]!="[": #pop all character before upto this "("
                    chars = stack.pop() + chars
                stack.pop() #as a moment when stack top is open paranthesis pop them means we will get all character from open to close

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*chars)
        return "".join(stack)