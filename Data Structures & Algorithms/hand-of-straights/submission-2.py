from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = {}
        for card in hand:
            counter[card] = counter.get(card,0)+1
        for key in sorted(counter):
            if counter[key]>0:
                freq= counter[key]
                for i in range(key,key+groupSize):
                    if counter.get(i,0)<freq:
                        return False
                    counter[i] -=freq
        return True
            

        