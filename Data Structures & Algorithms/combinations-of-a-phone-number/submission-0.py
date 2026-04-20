class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(index,path):
            if not digits:
                return []
            if index == len(digits): #at max we are allowed to number of digits that many characters into result
                result.append("".join(path[:]))
                return 
            for letter in mapping[digits[index]]:
                path.append(letter)
                backtrack(index+1,path)
                path.pop()
        backtrack(0,[])
        return result 