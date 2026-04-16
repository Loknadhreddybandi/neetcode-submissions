import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,tsk in enumerate(tasks):
            tsk.append(i)
        tasks.sort(key=lambda x : x[0]) #sort based on start time
        min_heap = []
        i= 0
        time = 0
        res = []
        while min_heap or i<len(tasks): #there are tasks to process
            while i < len(tasks) and time >= tasks[i][0]: #process all tasks who are falling under time
                heapq.heappush(min_heap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not min_heap:#this is like we have a time but this time is lesser than start time of tasks since tasks are in sorted get the least starting time task and assign the value
                time = tasks[i][0]
            


            # heap has some tasks where their starting time falls under time and so we will pop them based on their processing and add this so time gets updated and next we will push tasks whose start time falls under this new time
            else:
                processing_time,indexx = heapq.heappop(min_heap)
                time += processing_time 
                res.append(indexx)   
        return res          


        