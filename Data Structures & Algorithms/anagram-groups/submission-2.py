class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count_s = frozenset(collections.Counter(s).items())
            res[count_s].append(s)
        return list(res.values())