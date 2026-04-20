class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(left,right):
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        result = []
        def backtrack(index,path):
            if index == len(s):#all characters taken and tehy are palindromes
                result.append(path[:])
                return 
            for i in range(index,len(s)):
                if is_palindrome(index,i):
                    path.append(s[index:i+1])
                    backtrack(i+1,path)
                    path.pop()
        backtrack(0,[])
        return result
        