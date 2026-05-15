class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            char1 = strs[0][i]
            for j in range(1,len(strs)):
                if i>= len(strs[j]) or  char1 != strs[j][i]:
                    return res
            res += char1
        return res