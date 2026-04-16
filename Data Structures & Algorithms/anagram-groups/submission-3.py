class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            counter = Counter(word)
            key = tuple(sorted(counter.items()))
            hashmap[key].append(word)
        return list(hashmap.values())

