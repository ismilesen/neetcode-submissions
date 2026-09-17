class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heapify the list in negative
        #pop from list until we  get to k
        #return abs kth 
        #problem of negative numbers going thru abs
        #we can use a hashmap that will have the indication
        #goes thru check before returning
        heap = []
        for i in range(len(nums)):
            if nums[i] <= 0:
                heap.append((-nums[i], "N"))
            else:
                heap.append((-nums[i], "P"))
        heapq.heapify(heap)
        for n in range(k - 1):
            heapq.heappop(heap)

        if heap[0][1] == "P":
            res = abs(heap[0][0])
        else:
            res = -heap[0][0]

        
        return res
