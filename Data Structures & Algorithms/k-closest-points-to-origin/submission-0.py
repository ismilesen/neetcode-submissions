class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #euclidean distance is (sqrt((x1 - x2)^2 + (y1 - y2)^2))
        #use this calculation with assessing points in comparison to (0, 0)
        closest = []
        #given each pair of points
        #do the calculation
        #then append into min heap
        #return the k first items which are the least by popping into our new array
        #list needs distances and points pairs

        for point in range(len(points)):
            x = points[point][0]
            
            y = points[point][1]
            
            distance = math.sqrt((0 - x)**2 + (0 - y)**2)
            heapq.heappush(closest, (distance, (x, y)))
            

        heapq.heapify(closest)

        res = []
        for i in range(k):
            distance, coordinates = heapq.heappop(closest)
            res.append(coordinates)
        return res