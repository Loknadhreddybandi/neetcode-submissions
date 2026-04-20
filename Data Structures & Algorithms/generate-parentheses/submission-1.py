class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(path, open_count, close_count):
            if open_count == n and close_count == n:    # valid → collect
                result.append("".join(path))
                return
            
            if open_count < n:                          # still have open left
                path.append("(")
                backtrack(path, open_count+1, close_count)
                path.pop()
            
            if close_count < open_count:                # unclosed brackets exist
                path.append(")")
                backtrack(path, open_count, close_count+1)
                path.pop()
        
        backtrack([], 0, 0)
        return result

