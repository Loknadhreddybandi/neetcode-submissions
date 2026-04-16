import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]
        distances = []
        for i in range(len(points)):
            first = points[i][0]
            second = points[i][1]
            distance = math.sqrt((first-origin[0])**2 + (second-origin[1])**2)
                       
            distances.append((distance,first,second))
        distances.sort()
        result = []
        for i in range(k):
            dist,first,second = distances[i]
            result.append((first,second))
        return result

        