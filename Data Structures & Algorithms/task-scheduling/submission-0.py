class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #need to track past tasks completed and how many cycles have went thru them
        #ok put everything into heap with freq
        #start with top of maxheap
        #store most recent task char
        #store how many cycles out of n
        #check most recent task and how many cycles out of n
        #hash with ("A", quantity, "n out of n")
        #once it reaches n reset
        #if not 0 then dont pop it
        #if all not zero then idle
    
        #Count the frequency of each task
        frequencies = Counter(tasks)
        #Build the list of tuples: (-frequency, 0, task_name)
        #note: We use negative frequency because Python's heapq is a min-heap by default.
        #Negating the values turns it into a max-heap (highest frequency first).
        max_heap = [-freq for freq in frequencies.values()]
        #Transform the list into a heap in-place
        heapq.heapify(max_heap)
        cycles = 0
        queue = deque()

        while max_heap or queue:
            cycles +=1

            if max_heap:
                freq = heapq.heappop(max_heap)
                newFreq = freq + 1
                if newFreq < 0:
                    queue.append((newFreq, cycles + n))
            else:
                pass

            if queue and queue[0][1] == cycles:
                ready_task_freq, _ = queue.popleft()
                heapq.heappush(max_heap, ready_task_freq)

        return cycles
            #put into queue char and freq






        

        