class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        filled_gas = 0
        for i in range(len(gas)):
            filled_gas += gas[i]-cost[i]
            if filled_gas<0: # if we consider this as starting point we cannot fill or buy gas at next station
                filled_gas = 0
                start = i+1
        return start

        