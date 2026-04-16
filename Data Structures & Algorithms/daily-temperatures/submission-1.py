class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures): # this is index,temp
            while stack and stack[-1][0] < t:
                temp,index = stack.pop() #this returns temp , index
                res[index] = -(index-i)
            stack.append((t,i))
        return res


            





        
        