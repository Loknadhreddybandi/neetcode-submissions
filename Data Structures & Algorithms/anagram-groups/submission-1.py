class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs: # loop through the number of input strings
            count = [0]*26 # create a array of size 26 (a----z)
            for c in s: # loop through each character in input string
                count[ord(c)-ord('a')]+=1 # for each string count how many times this particular char appears
            res[tuple(count)].append(s) # use this count as key and value is same as input string (since this is a 2d list)
        return list(res.values()) # as per above where key is char count and value is group of anagrams