from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        if k>n:
            return False
        count_s2 = Counter(s2[0:k])
        count_s1 = Counter(s1)
        if count_s1 == count_s2:
            return True
        for right in range(k,len(s2)):
            left =  right - k
            remove_character = s2[left]
            count_s2[remove_character]-=1
            if count_s2[remove_character]==0:
                del count_s2[remove_character]
            add_char = s2[right]
            count_s2[add_char]+=1
            if count_s1 == count_s2:
                return True
        return False
        