class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            #collision happens when stack is not empty and top and ast are +ve and -ve
            while stack and stack[-1]>0 and ast<0:
                if abs(ast)> stack[-1]: #if ast has more value than top value remove top value and stays in a loop
                    stack.pop()
                    continue
                elif abs(ast)==stack[-1]: #if positive and negative are same remove stack.top
                    stack.pop()
                break # this is like collision but top value is greater than ast 
            else:
                stack.append(ast)
        return stack
        